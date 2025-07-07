from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

from handlers.buttons import BACK


class AdminServerCallback(CallbackData, prefix="admin_server"):
    action: str
    data: str


def build_manage_server_kb(
    server_name: str, cluster_name: str, enabled: bool
) -> InlineKeyboardMarkup:

    builder = InlineKeyboardBuilder()

    toggle_text = "🔴 Отключить" if enabled else "🟢 Включить"
    toggle_action = "disable" if enabled else "enable"

    builder.button(
        text=toggle_text,
        callback_data=AdminServerCallback(
            action=toggle_action, data=server_name
        ).pack(),
    )

    builder.button(
        text="📈 Задать лимит",
        callback_data=AdminServerCallback(action="set_limit", data=server_name).pack(),
    )

    builder.button(
        text="🗑️ Удалить",
        callback_data=AdminServerCallback(action="delete", data=server_name).pack(),
    )

    builder.button(
        text="✏️ Сменить название",
        callback_data=AdminServerCallback(action="rename", data=server_name).pack(),
    )

    builder.button(
        text="🔙 Назад",
        callback_data=f"cluster_servers|{cluster_name}",
    )

    builder.adjust(1)
    return builder.as_markup()
