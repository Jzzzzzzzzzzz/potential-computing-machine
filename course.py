import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json

url = "http://www.cbr.ru/scripts/XML_daily.asp?"

today = datetime.today()
today = today.strftime("%d/%m/%Y")
payload = {"date_req": today}
response = requests.get(url,payload)
xml = BeautifulSoup(response.content,"html")
def get_valute(id):
    a = xml.find("valute", {"id": id}).value.text

    if id == "R01035":
       # print(a)
        return (f"За 1 шт Стерлиногов Соединнёного Королества стоит {a} рублей")

    elif id == "R01235":
        return (f"1 шт Доллар(США) стоит {a} рублей")
    elif id =="R01239":
        return (f"1 шт Евро стоит {a} рублей")


print(get_valute("R01035"))