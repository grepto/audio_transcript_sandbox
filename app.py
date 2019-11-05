import logging

from envparse import env
from telegram.ext import CommandHandler, MessageHandler, Updater
from telegram.ext.filters import Filters

from google_cloud_spech import transcribe_stream
from helpers import get_file

env.read_envfile()

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

REQUEST_KWARGS = dict()
if env('TELEGRAM_PROXY', default=None):
    REQUEST_KWARGS['proxy_url'] = env('TELEGRAM_PROXY')


def start(bot, update):
    update.message.reply_text('Hi!')


def help(bot, update):
    update.message.reply_text('Help!')


def send_echo(bot, update):
    update.message.reply_text(update.message.text)


def send_voice(bot, update):
    file = update.message.voice.get_file()
    voice = get_file(file)

    voice_text = transcribe_stream(voice.read())

    update.message.reply_text(voice_text)


updater = Updater(token=env('TELEGRAM_TOKEN'), request_kwargs=REQUEST_KWARGS)
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(MessageHandler(Filters.voice, send_voice))
dispatcher.add_handler(MessageHandler(Filters.text, send_echo))

if __name__ == '__main__':
    updater.start_polling()
