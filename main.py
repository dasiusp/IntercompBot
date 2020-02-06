import os

from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler
from datetime import datetime, time, timedelta, timezone

def mackenzie_callback(bot, update: Update, **optional_args):
    update.message.reply_text("O Mackenzie já voltou pro Intercomp?", quote=False)
    update.message.reply_markdown("**NÃO**", quote=False)


def cidade_callback(bot, update: Update, **optional_args):
    update.message.reply_text("Este ano, o Intercomp será em Rio Claro", quote=False)


def intercomp_callback(bot, update, **optional_args):
    update.message.reply_text("INTERCOMPE", quote=False)
    update.message.reply_text("PE", quote=False)
    update.message.reply_text("PE", quote=False)
    update.message.reply_text("ÔÔÔÔÔÔ", quote=False)


def contagem_callback(bot, update, **optional_args):
    def dateDiffInSeconds(date1, date2):
        timedelta = date2 - date1

        return timedelta.days * 24 * 3600 + timedelta.seconds

    def daysHoursMinutesSecondsFromSeconds(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return days, hours, minutes, seconds

    data_intercomp = datetime.strptime('2020-06-11 00:00:01', '%Y-%m-%d %H:%M:%S')

    now = datetime.now().astimezone(timezone(timedelta(hours=-3))) #Ajustando timezone para o padrão brasileiro (UTC-3)
    update.message.reply_text("FALTAM %d dias, %d horas, %d minutos e %d segundos pro INTERCOMP NINJA EDITION"
                              % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, data_intercomp)), quote=False)


def webhook(request):
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    dispatcher = Dispatcher(bot, None, 0)
    dispatcher.add_handler(CommandHandler("intercomp", intercomp_callback))
    dispatcher.add_handler(CommandHandler("contagem", contagem_callback))
    dispatcher.add_handler(CommandHandler("mackenzie", mackenzie_callback))
    dispatcher.add_handler(CommandHandler("cidade", cidade_callback))

    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return "ok"
