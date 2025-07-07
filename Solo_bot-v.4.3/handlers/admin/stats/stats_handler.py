from datetime import datetime, timedelta

import pytz
from aiogram import F, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import CallbackQuery, Message
from sqlalchemy.ext.asyncio import AsyncSession
from collections import Counter


from bot import bot
from config import ADMIN_ID
from database import (
    count_active_keys,
    count_total_keys,
    count_total_referrals,
    count_total_users,
    count_trial_keys,
    count_users_registered_between,
    count_users_registered_since,
    count_users_updated_today,
    get_tariff_distribution,
    get_tariff_names,
    get_tariff_groups,
    get_tariff_durations,
    sum_payments_between,
    sum_payments_since,
    sum_total_payments,
    count_hot_leads
)
from filters.admin import IsAdminFilter
from logger import logger
from utils.csv_export import (
    export_hot_leads_csv,
    export_keys_csv,
    export_payments_csv,
    export_users_csv,
)

from ..panel.keyboard import AdminPanelCallback, build_admin_back_kb
from .keyboard import build_stats_kb

router = Router()


@router.callback_query(AdminPanelCallback.filter(F.action == "stats"), IsAdminFilter())
async def handle_stats(callback_query: CallbackQuery, session: AsyncSession):
    try:
        now = datetime.utcnow()
        today = now.date()
        moscow_tz = pytz.timezone("Europe/Moscow")

        total_users = await count_total_users(session)
        users_updated_today = await count_users_updated_today(session, today)
        registrations_today = await count_users_registered_since(session, today)
        registrations_yesterday = await count_users_registered_between(
            session, today - timedelta(days=1), today
        )
        registrations_week = await count_users_registered_since(
            session, today - timedelta(days=today.weekday())
        )
        registrations_month = await count_users_registered_since(
            session, today.replace(day=1)
        )
        last_month_start = (today.replace(day=1) - timedelta(days=1)).replace(day=1)
        registrations_last_month = await count_users_registered_between(
            session, last_month_start, today.replace(day=1)
        )

        total_keys = await count_total_keys(session)
        active_keys = await count_active_keys(session)
        expired_keys = total_keys - active_keys
        trial_keys_count = await count_trial_keys(session)

        tariff_counts, no_tariff_keys = await get_tariff_distribution(session, include_unbound=True)
        tariff_names = await get_tariff_names(session, [tid for tid, _ in tariff_counts])
        tariff_groups = await get_tariff_groups(session, [tid for tid, _ in tariff_counts])
        tariff_durations = await get_tariff_durations(session, [tid for tid, _ in tariff_counts])

        grouped_tariffs = {}
        for tid, count in tariff_counts:
            group = tariff_groups.get(tid, "unknown")
            if group not in grouped_tariffs:
                grouped_tariffs[group] = []
            grouped_tariffs[group].append((tid, count))

        tariff_stats_text = ""
        duration_buckets = Counter()
        now_ts = int(datetime.utcnow().timestamp() * 1000)

        for key in no_tariff_keys:
            duration_days = round((key["expiry_time"] - now_ts) / (1000 * 60 * 60 * 24))
            if 25 <= duration_days <= 35:
                bucket = "Без тарифа: 1 мес"
            elif 80 <= duration_days <= 100:
                bucket = "Без тарифа: 3 мес"
            elif 170 <= duration_days <= 200:
                bucket = "Без тарифа: 6 мес"
            elif 350 <= duration_days <= 380:
                bucket = "Без тарифа: 12 мес"
            else:
                bucket = "Без тарифа: прочее"
            duration_buckets[bucket] += 1

        bucket_order = {
            "Без тарифа: 1 мес": 1,
            "Без тарифа: 3 мес": 2,
            "Без тарифа: 6 мес": 3,
            "Без тарифа: 12 мес": 4,
            "Без тарифа: прочее": 5
        }
        sorted_buckets = sorted(
            duration_buckets.items(),
            key=lambda x: bucket_order.get(x[0], 999)
        )

        for name, count in sorted_buckets:
            tariff_stats_text += f"├ {name}: <b>{count}</b>\n"

        for group, tariffs in grouped_tariffs.items():
            tariff_stats_text += f"Тариф {group}\n"
            sorted_tariffs = sorted(
                tariffs,
                key=lambda x: tariff_durations.get(x[0], 0)
            )
            for tid, count in sorted_tariffs:
                name = tariff_names.get(tid, f"ID {tid}")
                tariff_stats_text += f" ├ {name}: <b>{count}</b>\n"

        tariff_stats_text = (
            "└ По тарифам и срокам:\n" + tariff_stats_text
            if tariff_stats_text
            else "└ Нет данных по тарифам\n"
        )

        total_referrals = await count_total_referrals(session)

        total_payments_today = await sum_payments_since(session, today)
        total_payments_yesterday = await sum_payments_between(
            session, today - timedelta(days=1), today
        )
        total_payments_week = await sum_payments_since(
            session, today - timedelta(days=today.weekday())
        )
        total_payments_month = await sum_payments_since(session, today.replace(day=1))
        total_payments_last_month = await sum_payments_between(
            session, last_month_start, today.replace(day=1)
        )
        total_payments_all_time = await sum_total_payments(session)
        hot_leads_count = await count_hot_leads(session)

        update_time = datetime.now(moscow_tz).strftime("%d.%m.%y %H:%M:%S")

        stats_message = (
            f"📊 <b>Статистика проекта</b>\n\n"
            f"👤 <b>Пользователи:</b>\n"
            f"<blockquote>"
            f"├ 🗓️ За день: <b>{registrations_today}</b>\n"
            f"├ 🗓️ Вчера: <b>{registrations_yesterday}</b>\n"
            f"├ 📆 За неделю: <b>{registrations_week}</b>\n"
            f"├ 🗓️ За месяц: <b>{registrations_month}</b>\n"
            f"├ 📅 За прошлый месяц: <b>{registrations_last_month}</b>\n"
            f"└ 🌐 Всего: <b>{total_users}</b>\n"
            f"</blockquote>\n"
            f"💡 <b>Активность:</b>\n"
            f"└ 👥 Сегодня были активны: <b>{users_updated_today}</b>\n\n"
            f"🤝 <b>Реферальная система:</b>\n"
            f"└ 👥 Всего привлечено: <b>{total_referrals}</b>\n\n"
            f"🔐 <b>Подписки:</b>\n"
            f"<blockquote>"
            f"├ 📦 Всего сгенерировано: <b>{total_keys}</b>\n"
            f"├ ✅ Активных: <b>{active_keys}</b>\n"
            f"├ ❌ Просроченных: <b>{expired_keys}</b>\n"
            f"├ 🧪 Триальных: <b>{trial_keys_count}</b>\n"
            f"{tariff_stats_text}"
            f"</blockquote>\n"
            f"💰 <b>Финансы:</b>\n"
            f"<blockquote>"
            f"├ 📅 За день: <b>{total_payments_today} ₽</b>\n"
            f"├ 📆 Вчера: <b>{total_payments_yesterday} ₽</b>\n"
            f"├ 📆 За неделю: <b>{total_payments_week} ₽</b>\n"
            f"├ 📆 За месяц: <b>{total_payments_month} ₽</b>\n"
            f"├ 📆 Прошлый месяц: <b>{total_payments_last_month} ₽</b>\n"
            f"└ 🏦 Всего: <b>{total_payments_all_time} ₽</b>\n"
            f"</blockquote>\n"
            f"🔥 <b>Горячие лиды: {hot_leads_count}</b>\n"
            f"⏱️ <i>Последнее обновление:</i> <code>{update_time}</code>"
        )

        await callback_query.message.edit_text(
            text=stats_message, reply_markup=build_stats_kb()
        )

    except TelegramBadRequest as e:
        if "message is not modified" not in str(e):
            logger.error(f"Error in user_stats_menu: {e}")
    except Exception as e:
        logger.error(f"Error in user_stats_menu: {e}")
        await callback_query.answer(
            "Произошла ошибка при получении статистики", show_alert=True
        )


@router.callback_query(
    AdminPanelCallback.filter(F.action == "stats_export_users_csv"), IsAdminFilter()
)
async def handle_export_users_csv(callback_query: CallbackQuery, session: AsyncSession):
    kb = build_admin_back_kb("stats")
    try:
        export = await export_users_csv(session)
        await callback_query.message.answer_document(
            document=export, caption="📅 Экспорт пользователей в CSV"
        )
    except Exception as e:
        logger.error(f"Ошибка при экспорте пользователей: {e}")
        await callback_query.message.edit_text(text=f"❗ Ошибка: {e}", reply_markup=kb)


@router.callback_query(
    AdminPanelCallback.filter(F.action == "stats_export_payments_csv"), IsAdminFilter()
)
async def handle_export_payments_csv(
    callback_query: CallbackQuery, session: AsyncSession
):
    kb = build_admin_back_kb("stats")
    try:
        export = await export_payments_csv(session)
        await callback_query.message.answer_document(
            document=export, caption="📅 Экспорт платежей в CSV"
        )
    except Exception as e:
        logger.error(f"Ошибка при экспорте платежей: {e}")
        await callback_query.message.edit_text(text=f"❗ Ошибка: {e}", reply_markup=kb)


@router.callback_query(
    AdminPanelCallback.filter(F.action == "stats_export_hot_leads_csv"), IsAdminFilter()
)
async def handle_export_hot_leads_csv(
    callback_query: CallbackQuery, session: AsyncSession
):
    kb = build_admin_back_kb("stats")
    try:
        export = await export_hot_leads_csv(session)
        await callback_query.message.answer_document(
            document=export, caption="📅 Экспорт горящих лидов"
        )
    except Exception as e:
        logger.error(f"Ошибка при экспорте горящих лидов: {e}")
        await callback_query.message.edit_text(text=f"❗ Ошибка: {e}", reply_markup=kb)


@router.callback_query(
    AdminPanelCallback.filter(F.action == "stats_export_keys_csv"), IsAdminFilter()
)
async def handle_export_keys_csv(callback_query: CallbackQuery, session: AsyncSession):
    kb = build_admin_back_kb("stats")
    try:
        export = await export_keys_csv(session)
        await callback_query.message.answer_document(
            document=export, caption="📅 Экспорт подписок в CSV"
        )
    except Exception as e:
        logger.error(f"Ошибка при экспорте подписок: {e}")
        await callback_query.message.edit_text(text=f"❗ Ошибка: {e}", reply_markup=kb)


async def send_daily_stats_report(session: AsyncSession):
    try:
        now_moscow = datetime.now(pytz.timezone("Europe/Moscow"))
        update_time = now_moscow.strftime("%d.%m.%y %H:%M")

        today = (
            pytz.timezone("Europe/Moscow")
            .localize(datetime.combine((now_moscow - timedelta(days=1)).date(), datetime.min.time()))
            .astimezone(pytz.UTC)
            .replace(tzinfo=None)
        )

        registrations_today = await count_users_registered_since(session, today)
        payments_today = await sum_payments_since(session, today)
        active_keys = await count_active_keys(session)

        text = (
            "🗓️ <b>Сводка за день</b>\n\n"
            f"👤 Новых пользователей: <b>{registrations_today}</b>\n"
            f"💰 Оплачено: <b>{payments_today} ₽</b>\n"
            f"🔐 Активных ключей: <b>{active_keys}</b>\n\n"
            f"⏱️ <i>{update_time} МСК</i>"
        )

        for admin_id in ADMIN_ID:
            await bot.send_message(admin_id, text)

    except Exception as e:
        logger.error(f"[Stats] Ошибка при отправке статистики: {e}")


@router.message(F.text == "Сводка", IsAdminFilter())
async def test_stats_command(message: Message, session: AsyncSession):
    await send_daily_stats_report(session)
