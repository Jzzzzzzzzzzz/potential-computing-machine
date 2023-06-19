'''var1=True
var2=False
print(type(var1))
var1=5>1
print(var1)


import  random
import time

#12-16
for i in range (5):
    hour = random.randint(1, 24)
    if hour > 12 and hour<=16 :
        print("День")
    elif hour >16 and hour <=23:
        print("Вечер")
    elif hour > 23 or hour <=4:
        print("Ночь")
    else:#hour > 3 and hour <=12
        print("Утро")
        time.sleep(0.5)'''
import requests
import json
#Отправляем запрос на сайт
response=requests.get("https://swapi.dev/api/")
#Преобразуем этот запрос в формат json(эта же переменная)
response=response.json()
#continue....
people_api=response.get("people")
planet_api=response.get("planets")
spaceships_api=response.get("starships")
url="https://swapi.dev/api/"

def check_people(url):
    for i in range(1,6):
        response=requests.get(f"{url}/{i}").json()#
        print(response)

def check_planets(url):
    a = []#Список в начале цикла для того стобы цикл его не обновлял
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
    print(dictionary[max_val_key])
        #print(type(response.get("diameter")))
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
check_planets(planet_api)
#check_spaceships(spaceships_api)
#check_people(people_api)#это и есть url,он его принимает


