import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

URL = "https://porsche.ua/models?category=911"
print(requests.get(URL).text)

MONGO_URL = "mongodb+srv://markkvu4:12345@cluster0.niyzzif.mongodb.net/?retryWrites=true&w=majority"

data = requests.get(URL).text

praices = soup = BeautifulSoup(data, features="html.parser")

cars = print(soup.find_all("div", {"class":"model-name"}))

print(soup.find_all("span", {"class":"val"}))

#for f in praices 0:10:
  #print(f.getText())

#for r in cars 0:10:
  #print(r.getText())

client = MongoClient(MONGO_URL)

db = client["Kvuch"]
praices = db["test"]
praices.insert_one({"praices":"test"})

