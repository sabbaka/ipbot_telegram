from telegram.ext import Updater
from telegram.ext import CommandHandler
import telegram
import netifaces
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


API_TOKEN = "API_KEY"
bot = telegram.Bot(token=API_TOKEN)

def getip():
    netifaces.ifaddresses('ETH_NAME')
    ip = netifaces.ifaddresses('ETH_NAME')[netifaces.AF_INET][0]['addr']
    return ip


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=getip())


def init():
    updater = Updater(API_TOKEN)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()


init()