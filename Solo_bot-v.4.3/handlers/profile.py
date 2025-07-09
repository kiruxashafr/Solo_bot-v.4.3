import html
import os

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message, InputMediaPhoto, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import (
    GIFT_BUTTON,
    INSTRUCTIONS_BUTTON,
    NEWS_MESSAGE,
    REFERRAL_BUTTON,
    SHOW_START_MENU_ONCE,
)
from database import get_balance, get_key_count, get_trial, get_keys
from handlers.buttons import (
    ABOUT_VPN,
    ADD_SUB,
    BACK,
    BALANCE,
    GIFTS,
    INSTRUCTIONS,
    INVITE,
    MAIN_MENU,
    MY_SUBS,
    TARIFF,
    TRIAL_SUB,
    IPHONE,
    ANDROID,
    PC,
    TV,
)
from handlers.texts import ADD_SUBSCRIPTION_HINT, CHOOSE_DEVICE_TEXT
from logger import logger

from .admin.panel.keyboard import AdminPanelCallback
from .texts import profile_message_send, tariff_message
from .utils import edit_or_send_message

router = Router()

@router.callback_query(F.data == "profile")
@router.message(F.text == "/profile")
@router.message(F.text == "/start")
async def process_callback_view_profile(
    callback_query_or_message: Message | CallbackQuery,
    state: FSMContext,
    admin: bool,
    session,
):
    if isinstance(callback_query_or_message, CallbackQuery):
        chat = callback_query_or_message.message.chat
        from_user = callback_query_or_message.from_user
        chat_id = chat.id
        target_message = callback_query_or_message.message
    else:
        chat = callback_query_or_message.chat
        from_user = callback_query_or_message.from_user
        chat_id = chat.id
        target_message = callback_query_or_message

    user = chat if chat.type == "private" else from_user

    if getattr(user, "full_name", None):
        username = html.escape(user.full_name)
    elif getattr(user, "first_name", None):
        username = html.escape(user.first_name)
    elif getattr(user, "username", None):
        username = "@" + html.escape(user.username)
    else:
        username = "Пользователь"

    image_path = os.path.join("img", "profile.jpg")
    logger.info(f"Переход в профиль. Используется изображение: {image_path}")

    key_count = await get_key_count(session, chat_id)
    balance = await get_balance(session, chat_id) or 0
    trial_status = await get_trial(session, chat_id)

    profile_message = profile_message_send(username, chat_id, int(balance), key_count)
    if key_count == 0:
        profile_message += ADD_SUBSCRIPTION_HINT
    else:
        profile_message += f"\n<blockquote> <i>{NEWS_MESSAGE}</i></blockquote>"

    builder = InlineKeyboardBuilder()
    # Первая строка: Мои подписки (если есть) и Добавить новую подписку
    row_buttons = []
    if key_count > 0:
        row_buttons.append(InlineKeyboardButton(text="☰ Мои подписки", callback_data="view_keys"))
    row_buttons.append(InlineKeyboardButton(text="✛ Купить VPN", callback_data="create_key"))
    builder.row(*row_buttons)

    # Вторая строка: Баланс
    builder.row(InlineKeyboardButton(text=BALANCE, callback_data="balance"))

    # Третья строка: Пригласить и Подарить (если включено)
    row_buttons = []
    if REFERRAL_BUTTON:
        row_buttons.append(InlineKeyboardButton(text="➤ Пригласить друга", callback_data="invite"))
    if GIFT_BUTTON:
        row_buttons.append(InlineKeyboardButton(text=GIFTS, callback_data="gifts"))
    if row_buttons:
        builder.row(*row_buttons)

    # Четвертая строка: Как подключить (если включено)
    if INSTRUCTIONS_BUTTON:
        builder.row(InlineKeyboardButton(text="？ Как подключить", callback_data="view_keys"))

    # Пятая строка: Админ-панель (если админ)
    if admin:
        builder.row(
            InlineKeyboardButton(
                text="◆ Администратор",  # Используем строгий символ
                callback_data=AdminPanelCallback(action="admin").pack(),
            )
        )

    # Шестая строка: Тарифы
    builder.row(InlineKeyboardButton(text=TARIFF, callback_data="tariff"))

    # Седьмая строка: О сервисе или Назад
    builder.row(InlineKeyboardButton(text="☰ Главное меню", callback_data="profile"))
    if SHOW_START_MENU_ONCE:
        builder.row(InlineKeyboardButton(text=ABOUT_VPN, callback_data="about_vpn"))
    else:
        builder.row(InlineKeyboardButton(text=BACK, callback_data="start"))

    await edit_or_send_message(
        target_message=target_message,
        text=profile_message,
        reply_markup=builder.as_markup(),
        media_path=image_path,
        disable_web_page_preview=False,
        force_text=True,
    )

@router.message(F.text == "/subs")
async def process_view_subscriptions(message: Message, state: FSMContext, session):
    chat_id = message.chat.id
    key_count = await get_key_count(session, chat_id)
    
    if key_count > 0:
        await message.answer("Переход к вашим подпискам...", reply_markup=InlineKeyboardBuilder().row(
            InlineKeyboardButton(text="☰ Мои подписки", callback_data="view_keys")
        ).as_markup())
    else:
        await message.answer("У вас нет активных подписок.", reply_markup=InlineKeyboardBuilder().row(
            InlineKeyboardButton(text="✛ Купить VPN", callback_data="create_key")
        ).as_markup())

@router.message(F.text == "/buy")
async def process_buy_vpn(message: Message, state: FSMContext):
    image_path = os.path.join("img", "tarif.jpg")
    logger.info(f"Переход в покупку VPN. Используется изображение: {image_path}")

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="✛ Купить VPN", callback_data="create_key"))
    builder.row(InlineKeyboardButton(text="☰ Главное меню", callback_data="profile"))

    await edit_or_send_message(
        target_message=message,
        text=tariff_message(),
        reply_markup=builder.as_markup(),
        media_path=image_path,
        disable_web_page_preview=False,
        force_text=False,
    )

@router.message(F.text == "/invite")
async def process_invite_friend(message: Message, state: FSMContext):
    if REFERRAL_BUTTON:
        await message.answer("Переход к приглашению друга...", reply_markup=InlineKeyboardBuilder().row(
            InlineKeyboardButton(text="➤ Пригласить друга", callback_data="invite")
        ).as_markup())
    else:
        await message.answer("Функция приглашения временно недоступна.")

@router.message(F.text == "/help")
async def process_help(message: Message, state: FSMContext, session):
    chat_id = message.chat.id
    key_count = await get_key_count(session, chat_id)
    
    if key_count == 0:
        await message.answer(
            "К сожалению, у вас пока что нет подписки.",
            reply_markup=InlineKeyboardBuilder().row(
                InlineKeyboardButton(text="✛ Купить VPN", callback_data="create_key"),
                InlineKeyboardButton(text="☰ Главное меню", callback_data="profile")
            ).as_markup()
        )
        return

    # Если подписка есть, получаем email первой подписки
    try:
        records = await get_keys(session, chat_id)
        if records:
            key_name = records[0].email  # Берем email первой подписки
            builder = InlineKeyboardBuilder()
            builder.row(
                InlineKeyboardButton(text=IPHONE, callback_data=f"connect_ios|{key_name}")
            )
            builder.row(
                InlineKeyboardButton(text=ANDROID, callback_data=f"connect_android|{key_name}")
            )
            builder.row(
                InlineKeyboardButton(text=PC, callback_data=f"connect_pc|{key_name}")
            )
            builder.row(
                InlineKeyboardButton(text=TV, callback_data=f"connect_tv|{key_name}")
            )
            builder.row(
                InlineKeyboardButton(text=BACK, callback_data=f"view_key|{key_name}")
            )

            await message.answer(
                CHOOSE_DEVICE_TEXT,
                reply_markup=builder.as_markup()
            )
        else:
            await message.answer(
                "К сожалению, у вас пока что нет подписки.",
                reply_markup=InlineKeyboardBuilder().row(
                    InlineKeyboardButton(text="✛ Купить VPN", callback_data="create_key"),
                    InlineKeyboardButton(text="☰ Главное меню", callback_data="profile")
                ).as_markup()
            )
    except Exception as e:
        logger.error(f"Ошибка при обработке команды /help: {e}")
        await message.answer("❌ Произошла ошибка. Попробуйте позже.")

@router.callback_query(F.data == "tariff")
async def process_callback_view_tariff(callback_query: CallbackQuery, state: FSMContext):
    image_path = os.path.join("img", "tarif.jpg")
    logger.info(f"Переход в тарифы. Используется изображение: {image_path}")

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text="✛ Купить VPN", callback_data="create_key"))
    builder.row(InlineKeyboardButton(text="☰ Главное меню", callback_data="profile"))

    try:
        await callback_query.message.edit_media(
            media=InputMediaPhoto(
                media=FSInputFile(image_path),
                caption=tariff_message(),
                parse_mode="HTML"
            ),
            reply_markup=builder.as_markup()
        )
    except Exception as e:
        logger.error(f"Ошибка при редактировании сообщения: {e}")
        await edit_or_send_message(
            target_message=callback_query.message,
            text=tariff_message(),
            reply_markup=builder.as_markup(),
            media_path=image_path,
            disable_web_page_preview=False,
            force_text=False,
        )

    await callback_query.answer()