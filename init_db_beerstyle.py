import requests
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient
client = MongoClient('localhost', 27017) # client가 robo와 같은 역할(mongodb에 연결)
db = client.your_beer_is


target_url = 'https://dev.bjcp.org/beer-styles/15a-weizenweissbier/'


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(target_url, headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

beer_style = soup.select('#content > div > article')

 
    title_tag = beer_style.select_one('header > h1')
        # info_tag = beer_style.select_one('div > p')
        # IBU_tag = beer_style.select_one('div > div.vital-statistics > div > div:nth-child(1) > div:nth-child(2) > p')
        # ABV_tag = beer_style.select_one('div > div.vital-statistics > div > div:nth-child(5) > div:nth-child(2) > p')
        # aroma_tag = beer_style.select_one('div > div.aroma > p:nth-child(2)')
        # flavor_tag = beer_style.select_one('div > div.flavor > p:nth-child(2)')
        # history_tag = beer_style.select_one('div > div.history > p')

    title = title_tag.text
        # info = info_tag.text
        # IBU = IBU_tag.text
        # ABV = ABV_tag.text
        # aroma = aroma_tag.text
        # flavor = flavor_tag.text
        # history = history_tag.text
        
        # document = {
        #     'title': title,
        #     'IBU': IBU,
        #     'ABV': ABV,
        #     'aroma': aroma,
        #     'flavor': flavor,
        #     'info': info,
        #     'history': history
        # }
        
        # db.bjcp.insert_one(document)


        print(title)

    # time.sleep(0.3)  # 0.3초 대기(차단당하지 않도록)
    # # print(beer_style)