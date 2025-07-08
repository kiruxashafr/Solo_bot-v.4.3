import html
import os

from aiogram import F, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery, InlineKeyboardButton, Message, InputMediaPhoto, FSInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder

from config import (
    INSTRUCTIONS_BUTTON,
    NEWS_MESSAGE,
    REFERRAL_BUTTON,
    SHOW_START_MENU_ONCE,
)
from database import get_balance, get_key_count, get_trial
from handlers.buttons import (
    ABOUT_VPN,
    ADD_SUB,
    BACK,
    BALANCE,
    INSTRUCTIONS,
    INVITE,
    MAIN_MENU,
    MY_SUBS,
    TARIFF,
    TRIAL_SUB,
)
from handlers.texts import ADD_SUBSCRIPTION_HINT
from logger import logger

from .admin.panel.keyboard import AdminPanelCallback
from .texts import profile_message_send, tariff_message
from .utils import edit_or_send_message

router = Router()

@router.callback_query(F.data == "profile")
@router.message(F.text == "/profile")
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
        row_buttons.append(InlineKeyboardButton(text=MY_SUBS, callback_data="view_keys"))
    row_buttons.append(InlineKeyboardButton(text=ADD_SUB, callback_data="create_key"))
    builder.row(*row_buttons)

    # Вторая строка: Баланс
    builder.row(InlineKeyboardButton(text=BALANCE, callback_data="balance"))

    # Третья строка: Пригласить (если включено)
    if REFERRAL_BUTTON:
        builder.row(InlineKeyboardButton(text=INVITE, callback_data="invite"))

    # Четвертая строка: Инструкции (если включено)
    if INSTRUCTIONS_BUTTON:
        builder.row(InlineKeyboardButton(text=INSTRUCTIONS, callback_data="instructions"))

    # Пятая строка: Админ-панель (если админ)
    if admin:
        builder.row(
            InlineKeyboardButton(
                text="◆ Администратор",
                callback_data=AdminPanelCallback(action="admin").pack(),
            )
        )

    # Шестая строка: Тарифы
    builder.row(InlineKeyboardButton(text=TARIFF, callback_data="tariff"))

    # Седьмая строка: О сервисе или Назад
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

@router.callback_query(F.data == "tariff")
async def process_callback_view_tariff(callback_query: CallbackQuery, state: FSMContext):
    image_path = os.path.join("img", "tarif.jpg")
    logger.info(f"Переход в тарифы. Используется изображение: {image_path}")

    builder = InlineKeyboardBuilder()
    builder.row(InlineKeyboardButton(text=ADD_SUB, callback_data="create_key"))
    builder.row(InlineKeyboardButton(text=MAIN_MENU, callback_data="profile"))

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
