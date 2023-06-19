import vk_api
from course import *
import requests
import json
token="vk1.a.RLT0g7qrq6d0VIQbBg64L9GkT9tBvvAP1a9_bGZE5sdoeqtprzY7dtODAAv51G0XQdDPsoKB8ZEbmJycVdaploYNAUQlgT43fAMzHx3DN4yxl9Y3S4sg5QB4AFhp4VFNqO0sotYCp8CgSmsOZO17qt66NVWe_mdiBX6AlseXEc9-62168QmoLq27HcNuFqJKtSCDjGsEiie1657tON1gCw"
vk=vk_api.VkApi(token=token)
response=requests.get("https://swapi.dev/api/").json()
planet_api=response.get("planets")
spaceships_api=response.get("starships")
url="https://swapi.dev/api/"
def check_planets(url):
    #Список в начале цикла для того стобы цикл его не обновлял
    a = []
    b = []
    for i in range(1,6):
        response=requests.get(f"{url}/{i}").json()#
        Name_of_planet=(response.get("name"))
        Diameter=(response.get("diameter"))
        a.append(Name_of_planet)
        b.append(Diameter)
    #print(a,b)
    Q=[]
    for i in b:
        Q.append(int(i))
    #Преобразуем словарь из двух списков a and Q
    dictionary=dict(zip(a,Q))
    print(dictionary)
    max_value=max(dictionary.values())
    #нашёл такой интересный метод извлечения ключа,только не до конца понял как он работает
    max_val_key = max(dictionary, key=dictionary.get )#я про это
    print(f"{dictionary[max_val_key]} {max_val_key}")
    return (f"{dictionary[max_val_key]} {max_val_key}")

def check_spaceships(url):
    response_1 = requests.get(f"{url}/{2}").json()
    n1=response_1.get("name")
    response_2 = requests.get(f"{url}/{3}").json()
    n2=response_2.get("name")
    response_3 = requests.get(f"{url}/{5}").json()
    n3=response_3.get("name")
    response_4 = requests.get(f"{url}/{10}").json()
    n4=response_4.get("name")
    response_5= requests.get(f"{url}/{12}").json()
    n5=response_5.get("name")
    a =[response_1.get("max_atmosphering_speed"),response_2.get("max_atmosphering_speed"),response_3.get("max_atmosphering_speed"),response_4.get("max_atmosphering_speed"),response_5.get("max_atmosphering_speed")]
    n = []
    for i in a:
        d=int(i)
        n.append(d)
    '''for i in range(6):
        print(f"{n[i-1]}-{n}{i}")
        n+=1'''

    print(n[0],"-",n1)
    print(n[1],"-",n2)
    print(n[2],"-",n3)
    print(n[3],"-",n4)
    print(n[4],"-",n5)
    MS=max(n)
    if n[0]==max(n):
        return (f"Максимальная скорость {n[0]}-{n1} ")
    elif  n[1]==max(n):
        return(f"Максимальная скорость {n[1]}-{n2} ")
    elif n[2] == max(n):
        return(f"Максимальная скорость {n[2]}-{n3} ")
    elif n[3] == max(n):
        return(f"Максимальная скорость {n[3]}-{n4} ")
    elif n[4]==max(n):
        return(f"Максимальная скорость {n[4]}-{n5} ")
    if n[4]==n[3]:
        return(f"Скорость {n4} такая же как у {n5} и равна {n[4]} ")



while True:
    messages = vk.method('messages.getConversations',{'count':20,'filter':'unanswered'})

    if messages["count"]>=1:

        #print(messeges["items"][0]["last_message"]["text"])
        user_id = messages["items"][0]["last_message"]["from_id"]
        message_id = messages["items"][0]["last_message"]["id"]
        message_text = messages["items"][0]["last_message"]["text"]
        if message_text=="привет":
            vk.method("messages.send",{"peer_id":user_id,"random_id":message_id,"message":"привет"})

        elif message_text=="курс доллара":
            vk.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message": get_valute("R01235")})
        elif message_text=="Планеты":
            vk.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message":check_planets(planet_api)})
        elif message_text=="Корабли":
            vk.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message":check_spaceships(spaceships_api)})
        else:
            vk.method("messages.send", {"peer_id": user_id, "random_id": message_id, "message":"Нет доступа"})





#До встречи!!!!Удачи!!)!!!!!



