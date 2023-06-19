import random

import vk_api
from   vk_api.longpoll import VkLongPoll,VkEventType
from course import *
from  wikiped import get_wikiped_article
import requests
import json

token="vk1.a.RLT0g7qrq6d0VIQbBg64L9GkT9tBvvAP1a9_bGZE5sdoeqtprzY7dtODAAv51G0XQdDPsoKB8ZEbmJycVdaploYNAUQlgT43fAMzHx3DN4yxl9Y3S4sg5QB4AFhp4VFNqO0sotYCp8CgSmsOZO17qt66NVWe_mdiBX6AlseXEc9-62168QmoLq27HcNuFqJKtSCDjGsEiie1657tON1gCw"
vk_session=vk_api.VkApi(token=token)
vk=vk_session.get_api()

longpoll=VkLongPoll(vk_session)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        msg = event.text
        user_id = event.user_id
        random_id = random.randint(1,10**10)


        if msg=="-к":
            response = "Какой курс ваолюты вы бы хотели посмотреть?(Евро,Доллар,Фунт стерлингов Соединенного королевства?)"#Не смог сделать для каждой валюты,хотел спарсить поочерёдно,но не получается!!!Сделал просто так.
        elif msg == "Доллар":
            response = (f"{get_valute('R01235')} рублей за 1 доллар")
        elif msg == "Евро":
            response = (f"{get_valute('R01239')} рублей за 1 евро")
        elif msg == "Фунт стерлингов Соединенного королевства":
            response = (f"{get_valute('R01035')} рублей за 1 фунт стерлингов Соединенного королевства")

      # elif msg=="Картинки":
           # cat = str(random.randint(1, 10))
            #cat_img = open("C:/Users/Tom/PycharmProjects/pythonProject2/img/" + cat + ".jpg", "rb")
            #response = cat_img

        elif msg.startswith("-в"):

            article = msg[2:]
            response = get_wikiped_article(article)
        else:
            response = "Нет доступа"

        vk.messages.send(user_id=user_id,random_id=random_id,message=response)



        print(msg,user_id)

#До встречи!!!!Удачи!!!!!