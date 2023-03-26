import requests
from bs4 import BeautifulSoup

URL = "https://porsche.ua/models?category=911"
print(requests.get(URL).text)

MONGO_URL = "mongodb+srv://markkvu4:<12345>@cluster0.niyzzif.mongodb.net/?retryWrites=true&w=majority"

data = requests.get(URL).text

soup = BeautifulSoup(data, features="html.parser")

print(soup.find_all("div", {"class":"model-name"}))

print(soup.find_all("span", {"class":"val"}))

