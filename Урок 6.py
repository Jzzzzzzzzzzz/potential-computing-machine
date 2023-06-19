import requests
from bs4 import BeautifulSoup
from datetime import datetime

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}
response = requests.get(url,payload)
xml = BeautifulSoup(response.content,"html")
def get_valute(id):
     a=xml.find("valute",{"id":id}).value.text
     return a
print(get_valute("R01235")+"-доллар сегодня")
print(get_valute("R01215")+"-датская крона сегодня")
print(get_valute("R01239")+"-евро сегодня")
Euro = get_valute("R01239")
euro=float(Euro.replace(',', '.'))

Dollar = get_valute("R01235")
dollar=float(Dollar.replace(',', '.'))
print(dollar)
sum_Euro=float(input("Сумма Евро:"))
def convertor(euro,dollar,sum_Euro):
     sum_Euro=euro*sum_Euro
     dollar=sum_Euro/dollar
     return (f"{dollar} или округлим и получим примерно {int(dollar)} доллара(ов)")
print(convertor(euro,dollar,sum_Euro))
















'''me_file = open("file.txt","w")
me_file.write(get_valute("R01235")+"-Доллар на сегодня ")
me_file.close()
me_file = open("file.txt","r")
print(me_file.read())
me_file.close()'''
#Целую,удачи!И до встречи конечно!Целую!До встречи ёще раз!
