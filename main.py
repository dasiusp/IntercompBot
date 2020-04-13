import os
from datetime import datetime

from pytz import timezone
from telegram import Update, Bot
from telegram.ext import Dispatcher, CommandHandler


def mackenzie_callback(bot, update: Update, **optional_args):
    update.message.reply_text("O Mackenzie já voltou pro Intercomp?", quote=False)
    update.message.reply_markdown("**NÃO**", quote=False)


def cidade_callback(bot, update: Update, **optional_args):
    update.message.reply_text("Este ano, o Intercomp não será :(", quote=False)


def intercomp_callback(bot, update, **optional_args):
    update.message.reply_text("INTERCOMPE", quote=False)
    update.message.reply_text("PE", quote=False)
    update.message.reply_text("PE", quote=False)
    update.message.reply_text("ÔÔÔÔÔÔ", quote=False)

def mochila_callback(bot, update, **optional_args):
    update.message.reply_text("AAAAAAA", quote=False)
    update.message.reply_text("EU TÔ MALUCOOOO", quote=False)
    update.message.reply_text("ROUBARAM MINHA MOCHILAAA", quote=False)
    update.message.reply_text("PRETA DA NIKEEEEE", quote=False)

def contagem_callback(bot, update, **optional_args):
    def dateDiffInSeconds(date1, date2):
        timedelta = date2 - date1

        return timedelta.days * 24 * 3600 + timedelta.seconds

    def daysHoursMinutesSecondsFromSeconds(seconds):
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        days, hours = divmod(hours, 24)
        return days, hours, minutes, seconds

    fuso_horario_sp = timezone('America/Sao_Paulo')
    data_intercomp = datetime(year=2020, month=6, day=11, hour=0, minute=0, second=1, tzinfo=fuso_horario_sp)

    now = datetime.now().astimezone(fuso_horario_sp)
    update.message.reply_text("FALTAM 365 + %d dias, %d horas, %d minutos e %d segundos pro INTERCOMP NINJA EDITION"
                              % daysHoursMinutesSecondsFromSeconds(dateDiffInSeconds(now, data_intercomp)), quote=False)


def webhook(request):
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    dispatcher = Dispatcher(bot, None, 0)
    dispatcher.add_handler(CommandHandler("intercomp", intercomp_callback))
    dispatcher.add_handler(CommandHandler("contagem", contagem_callback))
    dispatcher.add_handler(CommandHandler("mackenzie", mackenzie_callback))
    dispatcher.add_handler(CommandHandler("cidade", cidade_callback))
    dispatcher.add_handler(CommandHandler("mochila", mochila_callback))

    if request.method == "POST":
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return "ok"
