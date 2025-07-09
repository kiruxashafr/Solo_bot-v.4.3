from config import (CHANNEL_EXISTS, CHANNEL_URL, DISCOUNT_ACTIVE_HOURS,
                    PROJECT_NAME, REFERRAL_BONUS_PERCENTAGES, RENEWAL_PRICES,
                    SUPPORT_CHAT_URL, USERNAME_BOT)

# Текст главного меню
WELCOME_TEXT = (
    f"<b>🎉 {PROJECT_NAME} — твой доступ в свободный интернет! 🌐✨</b>\n\n"
    "<blockquote>"
    "🚀 <b>Высокая скорость</b>\n"
    "🔄 <b>Стабильность</b>\n"
    "🌍 <b>Смена локаций</b>\n"
    "💬 <b>Отзывчивая поддержка</b>\n"
    "📱💻 <b>Для телефонов, компьютеров и планшетов</b>\n"
    f"💰 <b>Реферальная программа: {len(REFERRAL_BONUS_PERCENTAGES.keys())}-уровневая</b>\n"
    "</blockquote>\n\n"
    "<i>Попробуй наш VPN совершенно бесплатно 👇</i>"
)

# Тарифы
def tariff_message():
    return (
        "🚀 <b>Тарифы</b>\n\n"
        "Все подписки включают подключение до 5 устройств — одного аккаунта достаточно для всех ваших устройств.\n\n"
        "📅 <b>1 день</b> — 19₽\n"
        "📅 <b>7 дней</b> — 69₽\n"
        "📅 <b>1 месяц</b> — 169₽\n"
        "📅 <b>3 месяца</b> — 499₽ (скидка 5%)\n"
        "📅 <b>6 месяцев</b> — 899₽ (скидка 10%)\n"
        "📅 <b>12 месяцев</b> — 1599₽ (скидка 20% 🔥)\n\n"
        "🔒 <b>В подписку включено:</b>\n"
        "• YouTube без рекламы\n"
        "• Высокая скорость\n"
        "• Поддержка 24/7\n\n"
        "💬 Тысячи пользователей уже выбрали нас — подключайтесь и вы."
    )

# Описание сервиса
def get_about_vpn(bot_version: str):
    return (
        "<b>🌐 О VPN</b>\n\n"
        "<b>🚀 Высокоскоростные серверы</b>\n"
        "🌍 Мы используем высокоскоростные серверы в различных локациях для обеспечения стабильного и быстрого соединения.\n\n"
        "<b>🔐 Безопасность данных</b>\n"
        "🛡️ Для защиты ваших данных мы применяем новейшие протоколы шифрования, которые гарантируют вашу конфиденциальность.\n\n"
        "<b>🔑 Ваш ключ — ваша безопасность!</b>\n"
        "⚠️ Не передавайте своё шифрование сторонним лицам, чтобы избежать рисков.\n\n"
    )

# Инструкции по подключению
CHOOSE_DEVICE_TEXT = "📲💻📺 <b>Выберите устройство, которое хотите подключить:</b>"
INSTRUCTION_PC = (
    "<b>🖥 Инструкция по подключению Windows:</b>\n\n"
    "1. Скачайте и установите приложение по кнопке ниже\n"
    "2. Нажмите кнопку «Подключить» и откройте через приложение\n"
    "3. Наслаждайтесь безопасным интернетом 🌐"
)

INSTRUCTION_MACOS = (
    "<b>🖥 Инструкция по подключению MacOS:</b>\n\n"
    "1. Скачайте и установите приложение по кнопке ниже\n"
    "2. Нажмите кнопку «Подключить» и откройте через приложение\n"
    "3. Наслаждайтесь безопасным интернетом 🌐"
)

INSTRUCTIONS = (
    "📋 <b>Инструкции по использованию вашей подписки:</b>\n\n"
    "1. 📱 <b>Скачайте приложение для вашего устройства:</b>\n"
    "   - 🤖 <b>Для Android:</b> <a href='https://play.google.com/store/apps/details?id=com.v2raytun.android&hl=ru'>V2RayTun</a>\n"
    "   - 🍎 <b>Для iPhone:</b> <a href='https://apps.apple.com/ru/app/v2raytun/id6476628951'>V2RayTun</a>\n"
    "   - 💻 <b>Для Windows:</b> <a href='https://github.com/hiddify/hiddify-next/releases/download/v2.5.7/Hiddify-Windows-Setup-x64.exe'>Hiddify Next</a>\n\n"
    "2. 🔑 <b>Скопируйте предоставленную ссылку</b>, которую вы получили ранее.\n\n"
    "3. 📲 <b>Откройте приложение и нажмите на плюсик сверху справа.</b>\n\n"
    "4. 📋 <b>Выберите 'Вставить из буфера обмена' для добавления подписки.</b>\n\n"
    f"💬 Если у вас возникнут вопросы, не стесняйтесь обращаться в <a href='{SUPPORT_CHAT_URL}'>поддержку</a>."
)

SUBSCRIPTION_DESCRIPTION = """\
<b>Ваша подписка:</b>
<code>{key_link}</code>

<b>Подключите свое мобильное устройство в несколько простых шагов</b>
🍏 <b>Для iPhone:</b>
<blockquote>
- Нажмите кнопку 🍏Cкачать
- Скачайте наше приложение, установите его
- Вернитесь в бота, нажмите кнопку 🍏Подключить
- Ваша подписка добавится в приложение, включите
Приятного пользования!
</blockquote>
🤖 <b>Для Android:</b>
<blockquote>
- Нажмите кнопку 🤖Cкачать
- Скачайте наше приложение, установите его
- Вернитесь в бота, нажмите кнопку 🤖Подключить
- Ваша подписка добавится в приложение, включите
Приятного пользования!
</blockquote>
"""

CONNECT_TV_TEXT = (
    "<b>1.</b> Скачайте приложение из Google Play на ваш телевизор: \n"
    "<a href='https://play.google.com/store/apps/details?id=com.vpn4tv.hiddify'>VPN4TV</a>\n"
    "<b>Или</b> скачайте файл напрямую: \n"
    "<a href='https://vpn4tv.com/download/vpn4tv.apk'>VPN4TV APK</a>, чтобы установить приложение с флешки.\n\n"
    "<b>2.</b> Установите приложение.\n\n"
    "<i>После установки приложения, нажмите кнопку 'Продолжить' ниже 👇</i>"
)

SUBSCRIPTION_DETAILS_TEXT = (
    "<b>1.</b> Откройте приложение <b>VPN4TV</b> на вашем устройстве.\n"
    "<b>2.</b> Используйте камеру вашего телефона для сканирования QR-кода, который вы получили.\n"
    "<b>3.</b> Отправьте ссылку вашей подписки в бота.\n\n"
    "🔗 <b>Ваша ссылка:\n\n</b> <code>{subscription_link}</code>\n\n"
    "<i>Для более подробной инструкции воспользуйтесь кнопкой ниже:</i>"
)

IOS_DESCRIPTION_TEMPLATE = (
    "🔑 <b>Ваша подписка:</b>\n\n"
    "<code>{key_link}</code>\n\n"
    "📲 <b>Инструкция по подключению (iPhone):</b>\n\n"
    "1. Скачайте приложение по кнопке ниже\n"
    "2. Нажмите кнопку «Подключить» и откройте через приложение\n"
    "3. Наслаждайтесь безопасным интернетом 🌐"
)

ANDROID_DESCRIPTION_TEMPLATE = (
    "🔑 <b>Ваша подписка:</b>\n\n"
    "<code>{key_link}</code>\n\n"
    "🤖 <b>Инструкция по подключению (Android):</b>\n\n"
    "1. Установите приложение по кнопке ниже\n"
    "2. Нажмите кнопку «Подключить»\n"
    "3. Наслаждайтесь безопасным интернетом 🌐"
)


# Тексты профилей
def profile_message_send(username, tg_id, balance, key_count):
    if CHANNEL_EXISTS:
        profile_message = (
            f"👤 <b>Профиль: {username}</b>\n\n"
            f"<blockquote>"
            f"—— <b>ID:</b> <code>{tg_id}</code>\n"
            f"—— <b>Баланс:</b> {balance} RUB\n"
            f"—— <b>К-во устройств:</b> {key_count}\n"
            f"</blockquote>\n"
            f"👉 <a href='{CHANNEL_URL}'>Наш канал</a> 👈"
        )
    else:
        profile_message = (
            f"👤 <b>Профиль: {username}</b>\n\n"
            f"<blockquote>"
            f"—— <b>ID:</b> <code>{tg_id}</code>\n"
            f"—— <b>Баланс:</b> {balance} RUB\n"
            f"—— <b>К-во устройств:</b> {key_count}\n"
            f"</blockquote>\n\n"
        )
    return profile_message

ADD_SUBSCRIPTION_HINT = "\n<blockquote>🔧 <i>Нажмите кнопку ➕ Добавить новую подписку, чтобы настроить VPN-подключение</i></blockquote>"

# Тексты оплаты
PAYMENT_OPTIONS = [{'text': f'{price} RUB', 'callback_data': f'amount|{price}'} for price in RENEWAL_PRICES.values()]
PLAN_SELECTION_MSG = "📋 <b>Выберите план продления:</b>\n\n💰 <b>Баланс:</b> {balance} руб.\n\n📅 <b>Текущая дата истечения подписки:</b> {expiry_date} 🔑"
PAYMENT_SUCCESS_MESSAGE = "Ваш баланс успешно пополнен на {amount} руб.{cashback_text} Спасибо за оплату!"
AMOUNT_TEXT = "Выберите сумму пополнения:"
PAYMENT_METHODS_MSG = (
    "💸 <b>Выберите удобный способ пополнения баланса:</b>\n"
    "<blockquote>"
    "• Быстро и безопасно\n"
    "• Поддержка разных платежных систем\n"
    "• Моментальное зачисление средств 🚀\n"
    "</blockquote>"
)
BALANCE_MANAGEMENT_TEXT = "<b>Управление вашим балансом 💰</b>\n\nВаш баланс: {balance}"
BALANCE_HISTORY_HEADER = "📊 <b>Последние 3 операции с балансом:</b>\n\n"
DEFAULT_PAYMENT_MESSAGE = "Вы выбрали пополнение на {amount} рублей. Перейдите по ссылке для оплаты:"
DEFAULT_PAYMENT_TITLE = "Пополнение баланса"
ENTER_SUM = "Пожалуйста, введите сумму пополнения."
YOOMONEY_FAST_PAY_MSG = "💳 Для оплаты подписки на сумму <b>{amount}₽</b> нажмите кнопку ниже:"
CRYPTOBOT_DESCRIPTION = "Пополнение на {amount}₽"


# Тексты управления ключами
CREATING_CONNECTION_MSG = "⏳ Пожалуйста, подождите, создаем вам подключение..."
SELECT_TARIFF_PLAN_MSG = "💳 Выберите тарифный план для создания нового ключа:"
INSUFFICIENT_FUNDS_MSG = "💳 Недостаточно средств. Для продолжения необходимо пополнить баланс на {required_amount}₽."
SELECT_COUNTRY_MSG = "🌍 Пожалуйста, выберите страну для вашего ключа:"
NO_SUBSCRIPTIONS_MSG = "<b>🔑 У вас пока нет подписок.</b>\n\nВы можете создать новую подписку для подключения устройств."
FROZEN_SUBSCRIPTION_MSG = "Подписка заморожена.\nДата истечения будет обновлена после разморозки."
UNFREEZE_SUBSCRIPTION_CONFIRM_MSG = "Хотите включить (разморозить) подписку?\n\nПосле включения доступа трафик и время снова начнут расходоваться."
SUBSCRIPTION_UNFROZEN_MSG = "✅ Подписка успешно включена.\n\nТеперь трафик и время подписки будут расходоваться."
FREEZE_SUBSCRIPTION_CONFIRM_MSG = "Вы можете заморозить (отключить) свою подписку на любой удобный срок, если временно не будете пользоваться VPN. Включить обратно можно будет в этом же меню.\n\n<b>Вы уверены, что хотите заморозить подписку?</b>"
SUBSCRIPTION_FROZEN_MSG = "✅ Подписка успешно заморожена.\n\nЧтобы включить обратно, зайдите в меню ключа и нажмите «Включить подписку»."
DELETE_KEY_CONFIRM_MSG = "<b>Вы уверены, что хотите удалить ключ?</b>"
KEY_DELETED_MSG_SIMPLE = "Ключ успешно удален."
INSUFFICIENT_FUNDS_RENEWAL_MSG = "💳 Недостаточно средств. Пополните баланс на {required_amount}₽."

# Тексты подписок и ключей
KEY_MESSAGE = "📋 <b>Ваша подписка:\n\n</b> <code>{}</code>\n\n"

INSTRUCTIONS_TRIAL = (
    "📲 <b>Подключите устройство</b> через кнопку ниже — выберите вашу платформу (телефон, ТВ, ПК и т.д.) и следуйте простой инструкции.\n\n"
    "💬 Если у вас возникнут вопросы, не стесняйтесь обращаться в <a href='{SUPPORT_CHAT_URL}'>поддержку</a>."
)


def key_message_success(connection_link, tariff_name: str = "", traffic_limit: int = 0, device_limit: int = 0):
    key_message = (
        "✅ Подписка успешно создана: 🎉\n\n"
        f"<code>{connection_link}</code>\n\n"
    )
    tariff_lines = []
    if tariff_name:
        tariff_lines.append(f"🕒 Тариф: {tariff_name}")
    if traffic_limit is not None and traffic_limit > 0:
        tariff_lines.append(f"📊 Трафик: {traffic_limit} ГБ")
    if device_limit is not None and device_limit > 0:
        tariff_lines.append(f"📱 Лимит устройств: {device_limit}")
    if tariff_lines:
        key_message += "📦 Информация о тарифе:" + "<blockquote>" + "\n".join(tariff_lines) + "\n</blockquote>\n"
    key_message += "<i>Добавьте подписку в приложение — это просто:</i>\n\n"
    key_message += f"{INSTRUCTIONS_TRIAL}"
    return key_message


def key_message(key, formatted_expiry_date, days_left_message, server_name, country=None, hwid_count: int = 0, tariff_name: str = "", traffic_limit: int = 0, device_limit: int = 0):
    response_message = (
        f"🔑 <b>Ваша подписка:</b>\n\n"
        f"<code>{key}</code>\n\n"
    )
    tariff_lines = []
    if tariff_name:
        tariff_lines.append(f"🕒 Тариф: {tariff_name}")
    traffic = traffic_limit if traffic_limit is not None else 0
    devices = device_limit if device_limit is not None else 0
    if traffic > 0:
        tariff_lines.append(f"📊 Трафик: {traffic} ГБ")
    if devices > 0:
        tariff_lines.append(f"📱 Лимит устройств: {devices}")
    if tariff_lines:
        response_message += "📦 Информация о тарифе:" + "<blockquote>" + "\n".join(tariff_lines) + "\n</blockquote>\n"

    if device_limit is not None and device_limit > 0 and hwid_count > 0:
        response_message += f"\n📱 <b>Подключенных устройств:</b> {hwid_count}\n\n"

    response_message += (
        f"📅 <b>Статус подписки:</b>\n"
        f"<blockquote>{days_left_message}\n"
        f"🛑 Истекает: {formatted_expiry_date}</blockquote>\n"
    )
    
    if country:
        response_message += f"🌍 <b>Локация:</b> {country}\n"

    response_message += "\n<i>Подключите свое устройство по кнопкам ниже👇</i>"
    return response_message

# Уведомления о подписках и ключах
KEY_NOT_FOUND_MSG = "🔍 Подписка не найдена."
KEY_DELETED_MSG = (
    "Ваша подписка {email} была удалена, так как вы не продлили её действие.\n\n"
    "Перейдите в личный кабинет и получите новую!"
)
KEY_EXPIRED_DELAY_MSG = (
    "⚠️ Ваша подписка {email} истекла.\n\n"
    "Если вы не продлите её, она будет удалена через {time_formatted}."
)
KEY_EXPIRED_NO_DELAY_MSG = (
    "⚠ Ваша подписка {email} истекла!\n\n"
    "Продлите доступ, чтобы возобновить услуги."
)

def get_renewal_message(tariff_name: str = "", traffic_limit: int = 0, device_limit: int = 0, expiry_date: str = "") -> str:
    response_message = "✅ Ваша подписка была успешно продлена"
    
    tariff_lines = []
    if tariff_name:
        tariff_lines.append(f"🕒 Тариф: {tariff_name}")
    if traffic_limit is not None and traffic_limit > 0:
        tariff_lines.append(f"📊 Трафик: {traffic_limit} ГБ")
    if device_limit is not None and device_limit > 0:
        tariff_lines.append(f"📱 Лимит устройств: {device_limit}")
    
    if tariff_lines:
        response_message += "\n\n📦 Информация о тарифе:" + "<blockquote>" + "\n".join(tariff_lines) + "\n</blockquote>"
    
    if expiry_date and expiry_date.strip():
        response_message += f"\n📅 Подписка продлена до <b>{expiry_date}</b>"
    
    return response_message
    
KEY_EXPIRY_10H = (
    "<b>Уведомление по подписке {email}:</b>\n\n"
    "<blockquote>{hours_left_formatted}\n"
    "Дата окончания: {formatted_expiry_date}</blockquote>\n\n"
    "<i>Успейте продлить выгодно, при истечении подписки доступ прекратится 👇</i>"
)
KEY_EXPIRY_24H = (
    "<b>Уведомление по подписке {email}:</b>\n\n"
    "Статус подписки:\n"
    "<blockquote>{hours_left_formatted}\n"
    "Дата окончания: {formatted_expiry_date}</blockquote>\n\n"
    "<i>Продлите подписку по кнопке ниже или она продлится автоматически всего на месяц при достаточном балансе 👇</i>"
)

# Уведомления о канале и подписке
SUBSCRIPTION_REQUIRED_MSG = f"Для использования бота, пожалуйста, подпишитесь на наш канал: {CHANNEL_URL}"
NOT_SUBSCRIBED_YET_MSG = "Вы еще не подписаны на канал!"
SUBSCRIPTION_CONFIRMED_MSG = "Подписка подтверждена!"
SUBSCRIPTION_CHECK_ERROR_MSG = "Ошибка проверки подписки, повторите попытку"

# Специальные уведомления
TRIAL_INACTIVE_FIRST_MSG = (
    "👋 <b>Привет, {display_name}!</b>\n\n"
    "<blockquote>"
    "🎉 У тебя есть бесплатный пробный период на {trial_time_formatted}!\n"
    "Не упусти возможность попробовать наш VPN прямо сейчас.\n"
    "</blockquote>"
    "Нажми на кнопку ниже, чтобы активировать пробный доступ! 👇"
)
TRIAL_INACTIVE_BONUS_MSG = (
    "<b>{display_name}</b>, у нас для тебя подарок! 🎁\n\n"
    "<blockquote>"
    "Мы добавили тебе +{extra_days_formatted} к пробному периоду!\n"
    "Теперь у тебя есть еще шанс протестировать наш VPN целых {total_days_formatted}!\n"
    "</blockquote>"
    "Нажми на кнопку ниже, чтобы активировать доступ с бонусом +{extra_days_formatted}! 👇"
)
ZERO_TRAFFIC_MSG = (
    "⚠ <b>Ваша VPN-подписка {email} активна, но трафик не используется.</b>\n\n"
    "<blockquote>Если у вас возникли сложности с подключением, "
    "нажмите кнопку ниже, чтобы связаться с поддержкой.</blockquote>\n\n"
    "🛠 Мы поможем вам разобраться! 💡"
)

FALLBACK_MESSAGE = (
    "🤖 <b>Я пока не умею отвечать на такие сообщения</b>\n\n"
    "<b>❓ У вас вопрос или возникли сложности?</b>\n"
    "Свяжитесь с нашей поддержкой — мы поможем как можно скорее.\n\n"
    "<b>🔐 Управление подпиской</b>\n"
    "Всё, что касается вашего VPN — тарифы, продления, подключение — доступно в <b>личном кабинете</b> 👇"
)


## Капча
CAPTCHA_EMOJIS = {
    "🐶": "собакой",  # Собака
    "🐱": "кошкой",  # Кошка
    "🐭": "мышью",  # Мышь
    "🐹": "хомяком",  # Хомяк
    "🐰": "кроликом",  # Кролик
    "🦊": "лисой",  # Лиса
    "🐻": "медведем",  # Медведь
    "🐼": "пандой",  # Панда
    "🐨": "коалой",  # Коала
    "🐯": "тигром",  # Тигр
    "🦁": "львом",  # Лев
    "🐮": "коровой",  # Корова
    "🐷": "свиньей",  # Свинья
    "🐸": "лягушкой",  # Лягушка
    "🐵": "обезьяной",  # Обезьяна
}

# Тексты реферальной программы
def get_referral_link(user_id):
    return f"https://t.me/{USERNAME_BOT}?start=referral_{user_id}"

INVITE_TEXT_NON_INLINE = "\nПриглашаю тебя пользоваться действительно быстрым VPN вместе:\n\n{referral_link}"

def invite_message_send(referral_link, referral_stats):
    invite_message = (
        f"👥 <b>Ваша реферальная ссылка:</b>\n\n"
        f"<code>{referral_link}</code>\n\n"
        f"🤝 <i>Приглашайте друзей и получайте крутые бонусы на каждом уровне! 💰</i>\n\n"
        "🏆 <b>Бонусы за приглашения:</b>\n"
        "<blockquote>"
        + "\n".join(
            [
                f"{level} уровень: 🌟 {int(percent * 100)}% бонуса"
                for level, percent in REFERRAL_BONUS_PERCENTAGES.items()
            ]
        )
        + "\n</blockquote>\n"
        f"📊 <b>Статистика приглашений:</b>\n"
        f"👥 Всего приглашено: {referral_stats['total_referrals']} человек\n\n"
        f"📈 <b>Детальная статистика по уровням:</b>\n"
        "<blockquote>"
        + "\n".join(
            [
                f"🔹 Уровень {level}: {stats['total']} - {int(REFERRAL_BONUS_PERCENTAGES[level] * 100)}%"
                for level, stats in referral_stats['referrals_by_level'].items()
            ]
        )
        + "\n</blockquote>\n"
        + f"💰 <b>Общий бонус от рефералов:</b> {referral_stats['total_referral_bonus']} RUB"
    )
    return invite_message

REFERRAL_SUCCESS_MSG = "Вы стали рефералом пользователя с ID {referrer_tg_id}"
NEW_REFERRAL_NOTIFICATION = "🎉 Ваш реферал {referred_id} успешно зарегистрировался!"

TOP_REFERRALS_TEXT = (
    "Здесь можно увидеть топ людей, которые пригласили наибольшее количество рефералов в сервис.\n\n"
    "<blockquote>{personal_block}</blockquote>\n\n"
    "<b>🏆 Топ-5 пригласивших:</b>\n\n"
    "<blockquote>{rows}</blockquote>"
)

REFERRAL_OFFERS = [
    {
        "title": "🎁 Бесплатный VPN на 3 дня",
        "description": "✨ Надежный VPN сервис бесплатно для тебя!",
        "message": "✅ Попробуй наш VPN сервис бесплатно на {trial_time} дня!\n⚡️ Быстрое подключение\n🔒 Безопасный доступ",
    },
    {
        "title": "🚀 Быстрый и безопасный VPN",
        "description": "🛡 Безопасный доступ к любым сайтам и сервисам",
        "message": "🌐 Открой для себя безграничный доступ к любым сайтам!\n⭐️ Попробуй {trial_time} дня бесплатно",
    },
    {
        "title": "🔒 Защищенный интернет",
        "description": "🔐 Безопасный доступ к сети без ограничений и блокировок",
        "message": "🛡 Защити свои данные и получи свободный доступ к интернету!\n✨ {trial_time} дня бесплатного тестового периода",
    },
]

# Тексты подарков
def get_gift_link(user_id, gift_id):
    return f"https://t.me/{USERNAME_BOT}?start=gift_{gift_id}_{user_id}"

SHARE_TEXT_TEMPLATE = (
    "🎁 Вам подарили VPN на <b>{months_text}</b>!\n\n"
    "📅 Доступно до: {expiry_time}\n\n"
    "🔗 <a href='{gift_link}'>Получить подарок</a>"
)


SHARE_TEXT_TEMPLATE_NOT_INLINE = (
    "🎁 Дарю тебе VPN на {months} месяцев!\n\n"
    "📅 Доступно до: {expiry_time}\n\n"
    "🔗 Чтобы получить, перейди по этой ссылке: {gift_link}"
)

def get_gift_confirmation_text(selected_months: str, price: int) -> str:
    return (
        f"<b>Подтверждение подарка:</b>\n"
        f"Подписка на <b>{selected_months} {'месяц' if selected_months == '1' else 'месяца' if int(selected_months) in [2, 3, 4] else 'месяцев'}</b>\n"
        f"Стоимость: <b>{price} рублей</b>\n\n"
        "Подтвердите дарение подписки."
    )

GIFT_CHOICE = "<b>Выберите срок подписки для подарка:</b>"

GIFT_ITEM_TEMPLATE = (
    "🎁 <b>{months} {months_text}</b>\n"
    "🕓 Истекает: <code>{expiry_time}</code>\n"
    "👤 Получатель: {recipient}\n"
    "✅ Использован: {is_used}\n"
    "<blockquote>{gift_link}</blockquote>\n\n"
)
MY_GIFT_MENU = "<b>Ваши подарки:</b>\n\n"


GIFTS_ABOUT = "<b>Дарите подарки и следите, чтобы они дошли до адресата! 🎄</b>"

GIFT_ALREADY_USED_OR_NOT_EXISTS_MSG = "Этот подарок уже был использован или не существует."

NO_GIFTS = "У вас нет подарков."

GIFT_DELETE = "Подарок удалён."
GIFT_ACTIVATED_TEXT = "🎉 Ваш подарок на {months} {months_text} активирован!"


# Тексты купонов
COUPON_INPUT_PROMPT = (
    "<b>🎫 Введите код купона:</b>\n\n"
    "📝 Пожалуйста, введите действующий код купона, который вы хотите активировать. 🔑"
)
COUPON_NOT_FOUND_MSG = (
    "<b>❌ Купон не найден</b> или его использование ограничено.\n🔒 Пожалуйста, проверьте код и попробуйте снова. 🔍"
)
COUPON_ALREADY_USED_MSG = (
    "<b>❌ Вы уже активировали этот купон.</b> 🚫 Купоны могут быть активированы только один раз. 🔒"
)
COUPON_ACTIVATED_SUCCESS_MSG = (
    "<b>✅ Купон успешно активирован! 🎉</b>\n\nНа ваш баланс добавлено <b>{coupon_amount} рублей</b> 💰."
)
COUPON_SUCCESS_MSG = "🎉 Ваш баланс пополнен на {amount} RUB по купону!"

# Тексты капчи
CAPTCHA_PROMPT_MSG = "🔒 Для подтверждения, что вы не робот, выберите кнопку с {correct_text}"


# Тексты рассылок горячих лидов
HOT_LEAD_MESSAGE = (
    "🔥 <b>«Хороший сервис не забывается.»</b>\n\n"
    "Вы уже были с нами — значит, знаете, как удобно и стабильно работает подключение.\n\n"
    "📉 Сейчас у вас нет активной подписки, но только для вас мы сохранили <b>специальные условия</b> — "
    "вернитесь и получите тариф со скидкой!\n\n"
    f"⏳ <b>Скидка действует {DISCOUNT_ACTIVE_HOURS} часов</b>. Повторное подключение — в один клик 👇"
)

HOT_LEAD_FINAL_MESSAGE = (
    "⚡️ <b>Последний шанс!</b>\n\n"
    "Вы так и не активировали подписку — поэтому мы приготовили для вас <b>ещё более выгодный тариф</b>.\n\n"
    f"🔥 <b>Эксклюзивная скидка доступна только {DISCOUNT_ACTIVE_HOURS} часов</b> с момента получения этого сообщения.\n\n"
    "👉 Нажмите ниже, чтобы воспользоваться последней возможностью со скидкой!"
)
DISCOUNT_TARIFF = "<b>🔥 Выберите тариф со скидкой:</b>"
DISCOUNT_TARIFF_MAX = "⚡ <b>Выберите тариф с максимальной скидкой:</b>"

HOT_LEAD_LOST_OPPORTUNITY = (
    "💨 <b>Срок действия скидки истёк</b>\n\n"
    "Похоже, вы немного опоздали — специальное предложение больше недоступно.\n"
    "Но не стоит расстраиваться! 🎯 Мы регулярно готовим новые акции и бонусы специально для вас.\n\n"
    "📲 Следите за обновлениями в боте — в следующий раз вы точно успеете!"
)

# Тексты блокировки торрентов
TORRENT_BLOCKED_MSG = (
    "⚠️ <b>Замечено использование торрентов</b> ⚠️\n\n"
    "<b>Уважаемый пользователь, мы обнаружили использование торрент-трафика в вашей подписке.</b>\n\n"
    "📋 <b>Детали:</b>"
    "<blockquote>"
    "• Подписка: <code>{username}</code>\n"
    "• Сервер: {country}\n"
    "• Время блокировки страны: <b>{duration} минут</b>"
    "</blockquote>\n\n"
    "❗️ <b>Важно:</b>\n"
    "• Возможно, вы забыли отключить торрент-клиент и сейчас качаете или раздаете торренты через VPN\n"
    "• Загрузка и раздача через торренты запрещена согласно правилам использования сервиса\n"
    "• Пожалуйста, полностью выключите торрент-клиент\n\n"
    "⏳ <b>После истечения времени блокировки доступ будет автоматически восстановлен.</b>\n\n"
    "⚠️ <b>Внимание:</b> При повторном использовании торрентов, блокировка будет применена снова."
)

TORRENT_UNBLOCKED_MSG = (
    "✅ <b>Доступ восстановлен</b>\n\n"
    "<b>Уважаемый пользователь, временные ограничения для вашей подписки сняты.</b>\n\n"
    "📋 <b>Детали:</b>"
    "<blockquote>"
    "• Подписка: <code>{username}</code>\n"
    "• Сервер: {country}"
    "</blockquote>\n\n"
    "💬 <b>Напоминание:</b>\n"
    "• Пожалуйста, воздержитесь от использования торрентов\n"
    "• Убедитесь, что торрент-клиент полностью выключен"
)
