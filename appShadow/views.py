from django.shortcuts import render
from django.http import HttpResponse
import telegram

# Create your views here.

def index(request):
    bot = telegram.Bot(token='747350126:AAFSlYXgWRmJ9HowkXvVBpxsA_ZgPSpxvMU')
    return HttpResponse(bot.get_me())
