import telegram


TELEGRAM_TOKEN = 'telegram-token'
TELEGRAM_CHAT_ID = 'chat-id'


def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except telegram.TelegramError:
        return False
    return True
