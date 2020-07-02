from selenium import webdriver
from bs4 import BeautifulSoup
import time
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.your_beer_is
#D:\chromedriver_win32 84
driver = webdriver.Chrome(r"D:\chromedriver")
driver.implicitly_wait(30)
driver.get('https://www.brewersfriend.com/homebrew/recipe/calculator')




driver.find_element_by_xpath('''/html/body/div[1517]/div/div/a''').click()

# driver.find_element_by_xpath('''//*[@id="calsetup"]/div/div[4]/div[2]/div/input''').click()
# time.sleep(1)
# driver.find_element_by_xpath(f'''//*[@id="calsetup"]/div/div[4]/div[2]/div/div[2]/div[{37}]''').click()
# time.sleep(1)
# driver.find_element_by_xpath(f'''//*[@id="calStatsGreyBar"]/div[2]/div[9]''').click()
# time.sleep(1)
# # 2~59 36 제외

# soup = BeautifulSoup(driver.page_source, 'html.parser')
# name_tag =soup.select_one('#calsetup > div > div.recipeEditRight > div:nth-child(2) > div > div.text')
# IBU_tag = soup.select_one('#calStatsGreyBar > div.appbounds.maxtoggle > div.row > div:nth-child(1) > div:nth-child(7) > span.statsStyle > span.ibuStyleTinseth')
# ABV_tag = soup.select_one('#calStatsGreyBar > div.appbounds.maxtoggle > div.row > div:nth-child(1) > div:nth-child(4) > span.statsStyle > span')
# info_text_tag = soup.select_one('#calStatsGreyBar > div.appbounds.maxtoggle > div.row > div:nth-child(1) > div:nth-child(19) > #currentStyleMatch')

# name = name_tag.text.split('.')[1]
# ABV = ABV_tag.text
# IBU = IBU_tag.text
# info = info_text_tag.text
    
# document = {
#     'name' : name,
#     'ABV': ABV,
#     'IBU': IBU,
#     'info': info,
#     }
# time.sleep(1)
#     # print(document)
# db.brewersfriend.insert_one(document)

for i in range(2, 36):
    
    driver.find_element_by_xpath('''//*[@id="calsetup"]/div/div[4]/div[2]/div/input''').click()
    time.sleep(1)
    driver.find_element_by_xpath(f'''//*[@id="calsetup"]/div/div[4]/div[2]/div/div[2]/div[{i}]''').click()
    time.sleep(1)
    driver.find_element_by_xpath(f'''//*[@id="calStatsGreyBar"]/div[2]/div[9]''').click()
    time.sleep(1)
# 2~59 36 제외

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    name_tag =soup.select_one('#calsetup > div > div.recipeEditRight > div:nth-child(2) > div > div.text')
    IBU_tag = soup.select_one('#calStatsGreyBar > div.appbounds.maxtoggle > div.row > div:nth-child(1) > div:nth-child(7) > span.statsStyle > span.ibuStyleTinseth')
    ABV_tag = soup.select_one('#calStatsGreyBar > div.appbounds.maxtoggle > div.row > div:nth-child(1) > div:nth-child(4) > span.statsStyle > span')
    info_text_tag = soup.select_one('#calStatsGreyBar > div.appbounds.maxtoggle > div.row > div:nth-child(1) > div:nth-child(19) > #currentStyleMatch')

    name = name_tag.text.split('.')[1]
    ABV = ABV_tag.text
    IBU = IBU_tag.text
    info = info_text_tag.text
    
    document = {
        'name' : name,
        'ABV': ABV,
        'IBU': IBU,
        'info': info,
    }
    time.sleep(1)
    # print(document)
    db.brewersfriend.insert_one(document)

for i in range(37, 60):
    
    driver.find_element_by_xpath('''//*[@id="calsetup"]/div/div[4]/div[2]/div/input''').click()
    time.sleep(1)
    driver.find_element_by_xpath(f'''//*[@id="calsetup"]/div/div[4]/div[2]/div/div[2]/div[{i}]''').click()
    time.sleep(1)
    driver.find_element_by_xpath(f'''//*[@id="calStatsGreyBar"]/div[2]/div[9]''').click()
    time.sleep(1)
# 2~59 36 제외

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    name_tag =soup.select_one('#calsetup > div > div.recipeEditRight > div:nth-child(2) > div > div.text')
    IBU_tag = soup.select_one('#calStatsGreyBar > div.appbounds.maxtoggle > div.row > div:nth-child(1) > div:nth-child(7) > span.statsStyle > span.ibuStyleTinseth')
    ABV_tag = soup.select_one('#calStatsGreyBar > div.appbounds.maxtoggle > div.row > div:nth-child(1) > div:nth-child(4) > span.statsStyle > span')
    info_text_tag = soup.select_one('#calStatsGreyBar > div.appbounds.maxtoggle > div.row > div:nth-child(1) > div:nth-child(19) > #currentStyleMatch')

    name = name_tag.text.split('.')[1]
    ABV = ABV_tag.text
    IBU = IBU_tag.text
    info = info_text_tag.text
    
    document = {
        'name' : name,
        'ABV': ABV,
        'IBU': IBU,
        'info': info,
    }
    time.sleep(1)
    # print(document)
    db.brewersfriend.insert_one(document)


