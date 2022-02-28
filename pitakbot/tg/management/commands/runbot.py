from django.core.management import BaseCommand

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from config.settings import TOKEN
from tg.views import *


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        updater = Updater(TOKEN)
        updater.dispatcher.add_handler(CommandHandler(command='start', filters=Filters.chat_type.private, callback=start))
        updater.dispatcher.add_handler(MessageHandler(filters=Filters.all & Filters.chat_type.private, callback=order))
        updater.dispatcher.add_handler(CallbackQueryHandler(inline))
        updater.start_polling()
        updater.idle()
