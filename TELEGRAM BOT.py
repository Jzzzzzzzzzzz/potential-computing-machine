import telebot
import requests
from bs4 import BeautifulSoup
import  random
token="5710026835:AAGaIC5wAdSJXPW-3kjwpEIjWIdUu27JsOM"
bot=telebot.TeleBot(token)


@bot.message_handler(commands=["facts"])
def get_fact(message):
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="p-2 clearfix"))
    bot.send_message(message.chat.id,fact.a.attrs["href"]+fact.text)


@bot.message_handler(commands=["events"])
def get_event(message):
    response = requests.get("https://kudago.com/msk/festival/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="post-title"))
    bot.send_message(message.chat.id, fact.a.attrs["href"] + fact.text)




@bot.message_handler(commands=["poem"])
def send_poem(message):
    send_poem="""
вышел заяц на крыльцо
посмотреть на утрецо.
Смотрит-дождик не идет,
Можно спрыгать в огород!
"""
    bot.send_message(message.chat.id, send_poem)



@bot.message_handler(content_types=["text"])
def get_message (message):
    get_do = """/poem-стишок 
/fact-какие-то факты
"""
    if message.text=="Привет":
        bot.send_message(message.chat.id,"""Привет.
Что умеет делать этот бот?""")

    elif message.text.lower()=="что умеет делать этот бот":
        bot.send_message(message.chat.id,get_do)

    elif message.text.lower()=="кто создал бота":
        bot.send_message(message.chat.id,"Дементьев Кирилл Денисович")
    elif message.text.lower()=="Пока":
        bot.send_message(message.chat.id, "До свидания")



bot.polling()

#До встречи,PYTHON! До встречи,люблю тебя,все языки программирования,знания и все-все хорошее! Ёще раз,до встречи!