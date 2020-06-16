import requests
from bs4 import BeautifulSoup


target_url = 'https://dev.bjcp.org/style/2015/beer/?'


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(target_url, headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

beer_styles = soup.select('#content > div > div.blog.paginated.home-loop > div > article')



for beer_style in beer_styles:
    title_tag = beer_style.select_one('header > h1 > a')

    title = title_tag.text()

print(title)