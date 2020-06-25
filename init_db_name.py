import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
client = MongoClient('localhost', 27017) # client가 robo와 같은 역할(mongodb에 연결)
db = client.your_beer_is

target_url = 'https://m.blog.naver.com/nbc64pjh/221988284164'


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(target_url, headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

beers = soup.select('#SE-2430502c-2d10-4494-baf5-eb675c5fd24d > div > div > div > table > tbody > tr')

for beer in beers:
    name_tag = beer.select_one('td > div > p > span')
    name = name_tag.text
    
    documnet = {
        'name': name,
    }
    print(document)