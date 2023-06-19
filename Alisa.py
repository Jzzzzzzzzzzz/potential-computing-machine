import webbrowser
import pyaudio
import speech_recognition as sr #Распознование речи
import pyttsx3 # из текста в речь
import webbrowser
import os
import random
import datetime
import requests
from bs4 import BeautifulSoup
r = sr.Recognizer()
voice = pyttsx3.init()
voice.say("Привет, я голосовой помощник")
voice.runAndWait()
url="https://www.filmpro.ru/materials/selections/74070"
response = requests.get(url)
xml = BeautifulSoup(response.content,"lxml")
Eizaveta_ = xml.find_all(class_="Title")

while True:
    with sr.Microphone(device_index=1) as  sourse:
        print("Скажите что-нибудь...")
        audio = r.listen(sourse)
    speech = r.recognize_google(audio,language="ru_RU").lower()
    print("Вы сказали:"+ speech)
    if speech.find("привет")>=0:
        ALICA=["Здравствуйте","Привет!","Салют!","Горячо приветствую!"]
        Alica=random.choice(ALICA)
        voice.say(Alica)
        voice.runAndWait()
    elif speech.find("фильмы")>=0:
        voice.say("Фильмы про Елизавету могу вам посоветовать")
        for i in Eizaveta_:
            i = i.text
            voice.say(i)
        voice.runAndWait()
    elif speech.find("google")>=0:
        webbrowser.open_new("https://www.google.ru/")
        voice.say("Открываю")
        voice.runAndWait()
    elif speech.find("youtube")>=0:
        webbrowser.open_new("https://www.youtube.com/")
        voice.say("Открываю")
        voice.runAndWait()
    elif speech.find("twitch") >= 0:
        webbrowser.open_new("https://www.twitch.tv/?lang=ru")
        voice.say("Открываю")
        voice.runAndWait()
    elif speech.find("файл")>=0:
        os.startfile("E:\PROJECT\Project")
        voice.say("Открываю, одну мили секунду")
        voice.runAndWait()
    elif speech.find("Какое сейчас время?")>=0:
        voice.say("111")
        voice.runAndWait()
    elif speech.find("пока")>=0:
        voice.say("пока")
        voice.runAndWait()
        break
    elif speech.find("что ты умеешь")>=0:
        voice.say("Пока я умею открывать ютуб,google и твич!И один файлик")
        voice.runAndWait()
    elif speech.find("спасибо")>=0:
        ALICa=["Всегда пожалуйста","Не за что","Пожалуйста","милости просим"]
        a=random.choice(ALICa)
        voice.say(a)
        voice.runAndWait()




#Пока,до встречи,целую,удачи!!!!!!!Всего наилучшего!!!!Всего наипрекраснейшего!!!!)!!!!!





