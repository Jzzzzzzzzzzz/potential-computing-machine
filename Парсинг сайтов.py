import requests
from bs4 import BeautifulSoup
import  random
def get_fact():
    response = requests.get("https://i-fakt.ru/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="p-2 clearfix"))
    #print(fact)
    print(fact.text)
    print(fact.a.attrs["href"])
def get_event():
    response = requests.get("https://kudago.com/msk/festival/")
    response = response.content
    html = BeautifulSoup(response, "html.parser")
    fact = random.choice(html.find_all(class_="post-title"))
    print(fact.text.strip())#проверить!
    print(fact.a.attrs["href"])
while True:
    print("Введите-0 если хотите выйти")
    print("Введите-1 если хотите факт")
    print("Событие-2")
    a=int(input("Выберети пункт меню(0,1,2):"))
    if a==0:
        break
    elif a==1:
        get_fact()
    else:
        get_event()


'''link=requests.get('http://www.columbia.edu/~fdc/sample.html')
response = link.content
soup=BeautifulSoup(response,"html.parser")
h3=soup.find_all("h3")
print(h3)'''
#еще у меня вопрос) Почему метод text не может вывести допустим все элементы списка h3??? Если бы я хотел вывести строки всех элементов тега h3 нужно было все ставить в цикл? Или какпомогите с объяснением)))
'''link=requests.get('https://webscraper.io/test-sites/e-commerce/ajax/product/499')
response = link.content
soup=BeautifulSoup(response,"html.parser")
PC=soup.find(class_="container test-site")
print(PC.text)'''
#почему тут работает метод text,а если написать find_all не будет работать,потому что это типо список с одним элементом?

'''link=requests.get('https://mk12.moekino.net/movies/dzhon-uik-2014-smotret-onlayn-762738')
response = link.content
soup=BeautifulSoup(response,"html.parser")
PC=soup.find(class_="header-search")
print(PC)'''

'''link=requests.get('https://pozdravok.com/pozdravleniya/prazdniki/den-materi/2.htm')
response=link.content
soup=BeautifulSoup(response,"html.parser")
for pars in soup.find_all("a"):#пока pars проходит по всем тегам(списку) <a>,выполняется pars.get........
    h3=str(pars.get("href"))
    print(h3)
'''
#целую вас,PYTHON and PYCHARM and all programming languages!!!!!!)

