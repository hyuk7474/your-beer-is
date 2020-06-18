import requests
from bs4 import BeautifulSoup
# from selenium import webdriver

# driver = webdriver.Chrome(r"C:\Users\LG\Downloads\chromedriver_win32\chromedriver")
# driver.implicitly_wait(3)
# driver.get('https://www.brewersfriend.com/homebrew/recipe/calculator')

# driver.find_element_by_class_name('text')
# driver.find_element_by_css_selector('#calsetup > div > div.recipeEditRight > div > div > div.text')

# driver.page_source

target_url = 'https://dev.bjcp.org/style/2015/beer/?'


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get(target_url, headers=headers)


soup = BeautifulSoup(data.text, 'html.parser')

beer_styles = soup.select('#content > div > div.blog.paginated.home-loop > div > article')

for beer_style in beer_styles:
    title_tag = beer_style.select_one('header > h1 > a')
    info_tag = beer_style.select_one('div > p')
    title = title_tag['title']
    
    print(info_tag.text)
    #content > div > div.blog.paginated.home-loop > div

# print(beer_style)