from selenium import webdriver
import cx_Oracle
import requests
import time
from bs4 import BeautifulSoup
#페이지 딜레이를 위한 라이브러리
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
#다나와 접속
url = "http://www.danawa.com/?src=adwords&kw=GA0000020&gclid=EAIaIQobChMIspmGg8HJ7AIVwdaWCh0HbgvsEAAYASAAEgLg9vD_BwE"
browser.get(url)

elem = browser.find_element_by_link_text("컴퓨터/노트북/조립PC").click()

time.sleep(1)
browser.find_element_by_class_name("category_all_dot").click()

time.sleep(1)
browser.find_element_by_xpath("//*[@id='categoryExplodeLayer11']/div[1]/div[2]/ul/li[1]/a").click()

time.sleep(2)
soup = BeautifulSoup(browser.page_source, "lxml")

#검색결과와 무관한 ad 광고를 제외한 태그 삭제 
product = soup.find_all("li", attrs = {"class":"prod_item prod_layer"})
dixt= {}
time.sleep(2)
for pd in product :
    
    title = pd.find("p", attrs = {"class":"prod_name"}).get_text().replace("\n","").replace("\t","").replace("인기 순위","")
    spec = pd.find("dl", attrs = {"class":"prod_spec_set"}).get_text().replace("\n","").replace("\t","").replace("상세 스펙","")

    list = spec.split(" / ")
        
    dixt[title] = list


for dix in dixt:
    print(dix)
    print(dixt[dix])
    print("-------------------------------------")



