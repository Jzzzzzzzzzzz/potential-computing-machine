import telebot
import requests
from bs4 import BeautifulSoup
import  random
from datetime import datetime
import webbrowser
import pyaudio
import speech_recognition as sr  # Распознование речи
import pyttsx3  # из текста в речь    import webbrowser
import os
import random



token="5710026835:AAGaIC5wAdSJXPW-3kjwpEIjWIdUu27JsOM"
bot=telebot.TeleBot(token)



@bot.message_handler(commands=["start","help","button"])
def get_welcome (message):
    welcome="Итак......."
    keyboard=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
    button_1 = telebot.types.KeyboardButton("Факт")
    button_2=telebot.types.KeyboardButton("Стих")
    button_3=telebot.types.KeyboardButton("Кот")
    button_4=telebot.types.KeyboardButton("Стикеры")
    button_5=telebot.types.KeyboardButton("Во что поиграть в этом году?")
    button_6=telebot.types.KeyboardButton("Курсы монет на сегодня")
    button_7 = telebot.types.KeyboardButton("Ассистент")
    keyboard.add(button_1,button_2, button_3,button_4,button_5,button_6,button_7)
    bot.send_message(message.chat.id,welcome,reply_markup=keyboard )


@bot.message_handler(commands=["button"])
def button(message):
    g = "Обязательно скажи пока!Иначе ляжет бот"
    keyboard = telebot.types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=False)
    button = telebot.types.KeyboardButton("Выйти назад")
    keyboard.add(button)
    bot.send_message(message.chat.id,g, reply_markup=keyboard)


@bot.message_handler(commands=["assistant"])
def assistant(message):
    button(message)
    r = sr.Recognizer()
    voice = pyttsx3.init()
    voice.say("Привет, я голосовой помощник")
    voice.runAndWait()
    url = "https://www.filmpro.ru/materials/selections/74070"
    response = requests.get(url)
    xml = BeautifulSoup(response.content, "lxml")
    Eizaveta_ = xml.find_all(class_="Title")
    while True:
        with sr.Microphone(device_index=1) as sourse:
            bot.send_message(message.chat.id, "Скажите что-нибудь....")
            print("Скажите что-нибудь...")
            audio = r.listen(sourse)
        speech = r.recognize_google(audio, language="ru_RU").lower()
        print("Вы сказали:" + speech)
        if message.text=="Выйти назад":
            break
        if speech.find("привет") >= 0:
            ALICA = ["Здравствуйте", "Привет!", "Салют!", "Горячо приветствую!"]
            Alica = random.choice(ALICA)
            voice.say(Alica)
            voice.runAndWait()
        elif speech.find("фильмы") >= 0:
            voice.say("Фильмы про Елизавету могу вам посоветовать")
            for i in Eizaveta_:
                i = i.text
                voice.say(i)
            voice.runAndWait()
        elif speech.find("google") >= 0:
            webbrowser.open_new("https://www.google.ru/")
            voice.say("Открываю")
            voice.runAndWait()
        elif speech.find("youtube") >= 0:
            webbrowser.open_new("https://www.youtube.com/")
            voice.say("Открываю")
            voice.runAndWait()
        elif speech.find("twitch") >= 0:
            webbrowser.open_new("https://www.twitch.tv/?lang=ru")
            voice.say("Открываю")
            voice.runAndWait()
        elif speech.find("файл") >= 0:
            os.startfile("E:\PROJECT\Project")
            voice.say("Открываю, одну мили секунду")
            voice.runAndWait()
        elif speech.find("Какое сейчас время?") >= 0:
            voice.say("111")
            voice.runAndWait()
        elif speech.find("пока") >= 0:
            voice.say("пока")
            voice.runAndWait()
            break
        elif speech.find("что ты умеешь") >= 0:
            voice.say("Пока я умею открывать ютуб,google и твич!И один файлик")
            voice.runAndWait()
        elif speech.find("спасибо") >= 0:
            ALICa = ["Всегда пожалуйста", "Не за что", "Пожалуйста", "милости просим"]
            a = random.choice(ALICa)
            voice.say(a)
            voice.runAndWait()








@bot.message_handler(commands=["valute"])
def Valute (message):
    hey="Смотрим..."
    keyboard=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
    button_1 = telebot.types.KeyboardButton("Доллар")
    button_2 = telebot.types.KeyboardButton("Датская крона")
    button_3 = telebot.types.KeyboardButton("Евро")
    keyboard.add(button_1, button_2, button_3)
    bot.send_message(message.chat.id,hey, reply_markup=keyboard)




@bot.message_handler(commands=["valute1"])
def Valute_1(message):
    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    payload = {"date_req": today}
    response = requests.get(url, payload)
    xml = BeautifulSoup(response.content, "html")
    def get_valute(id):
        a = xml.find("valute", {"id": id}).value.text
        return a
    b=get_valute("R01235")
    bot.send_message(message.chat.id, b)
    bot.send_message(message.chat.id,"Рублей")

@bot.message_handler(commands=["valute2"])
def Valute_2(message):

    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    payload = {"date_req": today}
    response = requests.get(url,payload)
    xml = BeautifulSoup(response.content, "lxml")

    def get_valute(id):
        a = xml.find("valute", {"id": id}).value.text
        return a

    a = get_valute("R01215")
    bot.send_message(message.chat.id, a)
    bot.send_message(message.chat.id, "Рублей")



@bot.message_handler(commands=["valute3"])
def Valute_3(message):
    url = "http://www.cbr.ru/scripts/XML_daily.asp?"
    today = datetime.today()
    today = today.strftime("%d/%m/%Y")
    payload = {"date_req": today}
    response = requests.get(url,payload)
    xml = BeautifulSoup(response.content, "lxml")

    def get_valute(id):
        a = xml.find("valute", {"id": id}).value.text
        return a

    a = get_valute("R01239")
    bot.send_message(message.chat.id, a)
    bot.send_message(message.chat.id, "Рублей")







@bot.message_handler(commands=["game"])
def get_game (message):
    welcome="Выберете жанр:"
    keyboard=telebot.types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True,one_time_keyboard=False)
    button_1 = telebot.types.KeyboardButton("Симулятор")
    button_2 = telebot.types.KeyboardButton("Тактика")
    button_3 = telebot.types.KeyboardButton("Экшен")
    button_4 = telebot.types.KeyboardButton("Выйти")
    keyboard.add(button_1, button_2, button_3,button_4)
    bot.send_message(message.chat.id,welcome,reply_markup=keyboard )

@bot.message_handler(commands=["game1"])
def sim(message):
    response = requests.get("https://www.igromania.ru/games/all/simulator/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    game = random.choice(html.find_all(class_="left-block"))
    bot.send_message(message.chat.id, game.text)

@bot.message_handler(commands=["game2"])
def tactical(message):
    response = requests.get("https://www.igromania.ru/games/all/tactic/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    game = random.choice(html.find_all(class_="left-block"))
    bot.send_message(message.chat.id, game.text)
@bot.message_handler(commands=["game3"])
def Akshen(message):
    response = requests.get("https://www.igromania.ru/games/all/action/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    game = random.choice(html.find_all(class_="left-block"))
    bot.send_message(message.chat.id, game.text)




@bot.message_handler(commands=["facts"])
def get_fact(message):
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="p-2 clearfix"))
    keyboard=telebot.types.InlineKeyboardMarkup(row_width=1)
    btn_url=telebot.types.InlineKeyboardButton("Перейти",fact.a.attrs["href"])
    keyboard.add(btn_url)
    bot.send_message(message.chat.id, fact.text, reply_markup=keyboard)



@bot.message_handler(commands=["game"])
def top_game(message):
    response=requests.get("https://www.igromania.ru/games/pc/all/2023/")
    response=response.content
    html=BeautifulSoup(response,"html.parser")
    game=random.choice(html.find_all(class_="left-block"))
    bot.send_message(message.chat.id, game.a.attrs["href"] + game.text)







@bot.message_handler(commands=["events"])
def get_event(message):
    response = requests.get("https://kudago.com/msk/festival/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="post-title"))
    bot.send_message(message.chat.id, fact.a.attrs["href"] + fact.text)





@bot.message_handler(commands=["poem"])
def send_poem(message):
    send_poem = """
    вышел заяц на крыльцо
    посмотреть на утрецо.
    Смотрит-дождик не идет,
    Можно спрыгать в огород!
    """


    a=["Стишки потом!","Потом стихи!","Со стишками позже!","""Ладно,держи 1 стишок:
вышел заяц на крыльцо
посмотреть на утрецо.
Смотрит-дождик не идет,
Можно спрыгать в огород!"""]
    i = random.choice(a)

    bot.send_message(message.chat.id, i)


@bot.message_handler(commands=["cat"])
def get_cat(message):
    cat = str(random.randint(1, 10))
    cat_img = open("C:/Users/Tom/PycharmProjects/pythonProject2/img/" + cat + ".jpg", "rb")
    bot.send_photo(message.chat.id, cat_img)


@bot.message_handler(commands=['sticker'])
def send_sticker(message):
    a=["CAACAgIAAxkBAAEHGV9jswX5ZFMIbkxzbuhKA-wWwfnSFAACmhQAAsnkkUnqr1sH9YtLZi0E","CAACAgIAAxkBAAEHGWNjswX-U9fnAAGlJcGNAdsbm3l1Sz4AAqYOAAKGRqlJEJPjPhA1fR4tBA","CAACAgIAAxkBAAEHGWFjswX83kz8CWqhFR0AAWtYM4McV1kAAjYWAAJcQNhL20Zu0t2Veg0tBA","CAACAgIAAxkBAAEHGW9jswd1H8nsmPgo6HjkL7NKgQ0Y_gACcgADPsM1K3zWu21oFMLFLQQ","CAACAgIAAxkBAAEHGXNjswekJjkNQohlMAgrIPG5W_gDZAACYAADPsM1K1EDR_8E0BuRLQQ","CAACAgIAAxkBAAEHGYFjswhc_Er3yGanoF-o3v3CWkeBZQACUA0AAii9mUg639XwNHDHKS0E"]
    i=random.choice(a)
    bot.send_sticker(message.chat.id,i )




@bot.message_handler(content_types=["text"])
def get_message (message):
    get_do = """/help
"""
    if message.text=="Привет":
        bot.send_message(message.chat.id,"""Привет.
Что умеет делать этот бот?""")

    elif message.text.lower()=="что умеет делать этот бот":
        bot.send_message(message.chat.id,get_do)
    elif message.text=="Факт":
        get_fact(message)
    elif message.text=="Стих":
        send_poem(message)
    elif message.text == "Кот":
        get_cat(message)
    elif message.text=="Стикеры":
        send_sticker(message)
    elif message.text=="Во что поиграть в этом году?":
        get_game(message)
    elif message.text=="Экшен":
        Akshen(message)
    elif message.text=="Тактика":
        tactical(message)
    elif message.text=="Симулятор":
        sim(message)
    elif message.text=="Выйти":
        get_welcome(message)
    elif message.text=="Курсы монет на сегодня":
        Valute(message)
    elif message.text=="Доллар":
        Valute_1(message)
    elif message.text=="Датская крона":
        Valute_2(message)
    elif message.text=="Евро":
        Valute_3(message)
    elif message.text=="Ассистент":
        assistant(message)
    elif message.text=="Выйти назад":
        get_welcome(message)


    elif message.text.lower()=="кто создал бота":
        bot.send_message(message.chat.id,"Дементьев Кирилл Денисович")
    elif message.text.lower()=="Пока":
        bot.send_message(message.chat.id, "До свидания")



bot.polling()
#До скорой встречи!!!



