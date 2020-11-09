from selenium import webdriver
import requests
import time
from bs4 import BeautifulSoup


#페이지 딜레이를 위한 라이브러리
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
#browser.maximize_window() #창 최대화

#다나와로 드렁가기
url = "http://www.danawa.com/?src=adwords&kw=GA0000020&gclid=EAIaIQobChMIspmGg8HJ7AIVwdaWCh0HbgvsEAAYASAAEgLg9vD_BwE"
browser.get(url)

#글자를 이용해서 태그를 찾아내는 기능
#find_element_link_text().click()

elem = browser.find_element_by_link_text("컴퓨터/노트북/조립PC").click()
#click을 할 경우 elements 시 다중 클릭 오류

#elem = browser.find_elements_by_class_name("depth1 dp_dot")
#카테고리 페이지 다중 클릭 불가로 카테고리 테이지로 이동하기

#아래 코드를 태그가 생성되면 실행되도록 설정한다
time.sleep(1)
browser.find_element_by_class_name("category_all_dot").click()

#WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"category_all_dot")))


time.sleep(1)
browser.find_element_by_xpath("//*[@id='categoryExplodeLayer11']/div[1]/div[2]/ul/li[1]/a").click()
    #browser.find_element_by_link_text("애플 맥북").click()

#WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.XPATH,"categoryExplodeLayer11"))).click()


#노트북 안에 모른 노트북 정보가 들어가 있으니 이를 페이지별로 크롤링한다.
###링크가 생기면 클릭하는 기능 또한 추가

#elem = WebDriverWait(browser, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME,"prod_layer")))
#첫번째 결과 엘레멘트를 통째로 xpath로 출력

#print(elem)

#browser.find_element_by_link_text("노트북/태블릿PC").onclick() #안나오는 데 왜 안나오지?

#카테 고리중 컴퓨터 노트북 > 노트북/테블릿 > 순차 클릭
#btn_cate_02 다 가져오고 해당 값 들을 반복문으로 돌린다

#browser.find_elements_by_class_name("btn_cate_02")[0].onclick()

#====selenim을 통해서 페이지 소스를 뽑아 왔으니 바로 soup으로 넣는다
time.sleep(2)
soup = BeautifulSoup(browser.page_source, "lxml")

#검색결과와 무관한 ad 광고를 제외한 태그 삭제 
product = soup.find_all("li", attrs = {"class":"prod_item prod_layer"})
#print(product)

#dixt = {}

dixt= {}
time.sleep(2)
for pd in product :
    
    title = pd.find("p", attrs = {"class":"prod_name"}).get_text().replace("\n","").replace("\t","").replace("인기 순위","")
    spec = pd.find("dl", attrs = {"class":"prod_spec_set"}).get_text().replace("\n","").replace("\t","").replace("상세 스펙","")

    list = spec.split(" / ")
    #print(list)
    
    dixt[title] = list

    #print(spec)
    #dixt[title] = spec





#print(dixt)

for dix in dixt:
    print(dix)
    print(dixt[dix])
    print("-------------------------------------")



#위 정보를 잘라도되고 그냥 통째로 넣어도 좋다.

#print(dixt)


#위 코드를 url에서 page만 변경해서 값을 넣는 코드로 변경하자. -> 안된다. page param 막혀있다 -> 한페이지에서 이동하는 듯
# 셀러리움 클릭 함수를 이용해서 접근하자. 반복문을 돌리자 인기순으로 5~6페이지까지를 진행해주는 함수
# 이후에는 VO에 입력
# 전처리해서 분석하는 부분 추가하기

