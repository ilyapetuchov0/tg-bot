from telegram.ext import Updater, InlineQueryHandler, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
import requests
import logging

centuries = {
    'XX': {
        1901: [
            "Событие 1 1901 года 20-го века",
            "Событие 2 1901 года 20-го века"
        ],
        1902: [
            "Событие 1 1902 года 20-го века",
            "Событие 2 1902 года 20-го века"
        ],
        1903: [
            "Событие 1 1903 года 20-го века",
            "Событие 2 1903 года 20-го века"
        ],
        1904: [
            "Событие 1 1904 года 20-го века",
            "Событие 2 1904 года 20-го века"
        ]
    },
    'XXI': {
        2001: [
            "Событие 1 2001 года 21-го века"
        ],
        2002: [
            "Событие 1 2002 года 21-го века",
            "Событие 2 2002 года 21-го века"
        ],
        2007: [
            "Никто никогда не вернется в 2007 год"
        ],
        2008: [
            "Событие 2008 года"
        ],
        2009: [
            "Событие 2009"
        ]
    }
}

event = None

year = None

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

def start(update, context):
     update.message.reply_text("Вас приветствует бот-помощник по подготовке к ЕГЭ по истории. \n"
                                "Введите /set_century чтобы пройти тест по выбранному веку")


def button(update, context):
    query = update.callback_query

    query.answer()

    current_century = query.data

    query.edit_message_text(text = f"Вы выбрали {current_century} век")

def set_century(update, context):

    keyboard = [
        [
            InlineKeyboardButton("XX век", callback_data='XX'),
            InlineKeyboardButton("XXI век", callback_data='XXI'),
        ],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    update.message.reply_text('Выберите век', reply_markup=reply_markup)


def main():
    updater = Updater('1568409861:AAF1mRdj-MDXVxiD2FNRWSaeUUDTu_NF544')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(button))
    dp.add_handler(CommandHandler('set_century', set_century))
    # dp.add_handler(MessageHandler(Filters.text & (~Filters.command), echo))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()