import requests
from bs4 import BeautifulSoup
import  random
response = requests.get("https://www.igromania.ru/games/all/simulator/")
response = response.content
html = BeautifulSoup(response, "html.parser")
game = random.choice(html.find_all(class_="left-block"))
print(game.text)