import os

from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler


def intercomp_callback(bot, update, **optional_args):
    update.message.reply_text("INTERCOMPE", quote=False)
    update.message.reply_text("PE", quote=False)
    update.message.reply_text("PE", quote=False)
    update.message.reply_text("ÔÔÔÔÔÔ", quote=False)


def webhook(request):
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    dispatcher = Dispatcher(bot, None, 0)
    dispatcher.add_handler(CommandHandler("intercomp", intercomp_callback))

    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return "ok"
