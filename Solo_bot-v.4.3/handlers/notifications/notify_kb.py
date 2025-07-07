from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from handlers.buttons import DISCOUNT_TARIFF, MAIN_MENU, MAX_DISCOUNT_TARIFF, RENEW_KEY


def build_notification_kb(email: str) -> InlineKeyboardMarkup:
    """
    Формирует inline-клавиатуру для уведомлений.
    Кнопки: "🔄 Продлить VPN" (callback_data содержит email) и "👤 Личный кабинет".
    """
    from aiogram.utils.keyboard import InlineKeyboardBuilder

    builder = InlineKeyboardBuilder()
    builder.button(text=RENEW_KEY, callback_data=f"renew_key|{email}")
    builder.button(text=MAIN_MENU, callback_data="profile")
    builder.adjust(1)
    return builder.as_markup()


def build_notification_expired_kb() -> InlineKeyboardMarkup:
    """
    Формирует inline-клавиатуру для уведомлений после удаления или продления.
    Кнопка: "👤 Личный кабинет"
    """
    from aiogram.utils.keyboard import InlineKeyboardBuilder

    builder = InlineKeyboardBuilder()
    builder.button(text=MAIN_MENU, callback_data="profile")
    return builder.as_markup()


def build_hot_lead_kb(final: bool = False) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(
                    text=DISCOUNT_TARIFF if not final else MAX_DISCOUNT_TARIFF,
                    callback_data=(
                        "hot_lead_discount" if not final else "hot_lead_final_discount"
                    ),
                )
            ]
        ]
    )


def build_tariffs_keyboard(
    tariffs: list[dict], prefix: str = "tariff"
) -> InlineKeyboardMarkup:
    buttons = [
        [
            InlineKeyboardButton(
                text=f"{t['name']} — {t['price_rub']}₽",
                callback_data=f"{prefix}|{t['id']}",
            )
        ]
        for t in tariffs
    ]

    return InlineKeyboardMarkup(inline_keyboard=buttons)
