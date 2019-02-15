from django.shortcuts import render
from django.http import HttpResponse
from telegram.ext import Updater
from telegram.ext import CommandHandler

# Create your views here.

def index(request):

    def start(bot, update):
        bot.sendMessage(chat_id=update.message.shat_id, text="Приветствую, Ням!")

    updater = Updater(token='747350126:AAFSlYXgWRmJ9HowkXvVBpxsA_ZgPSpxvMU')
    
    start_handler = CommandHandler('start', start)

    updater.dispatcher.add_handler(start_handler)
    updater.start_polling()
    
    return HttpResponse("Bot has been updated!")
