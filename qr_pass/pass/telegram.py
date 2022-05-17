import telegram


TELEGRAM_TOKEN = '5323147839:AAG4hmkSoKIVeSwJv3O81pfzCgnPGfjup-c'
TELEGRAM_CHAT_ID = '1684022747'


def send_message(message):
    bot = telegram.Bot(token=TELEGRAM_TOKEN)

    try:
        bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=message)
    except telegram.TelegramError:
        return False
    return True
