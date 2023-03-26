import requests
from bs4 import BeautifulSoup

URL = "https://porsche.ua/models?category=911"
print(requests.get(URL).text)

data = requests.get(URL).text

soup = BeautifulSoup(data, features="html.parser")

print(soup.find_all("td"))
