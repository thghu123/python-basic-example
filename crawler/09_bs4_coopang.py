import requests
import re
from bs4 import BeautifulSoup
#여기서 쿠팡과 달리 다나와는 전체 노트북 정보가 안나온다. 이를 셀러리움으로 해야한다.

url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=4&backgroundColor="
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

res = requests.get(url, headers = headers)
res.raise_for_status()
soup = BeautifulSoup(res.text,"lxml")

#print(res.text)

#광고 상품은 제외, 리뷰 100개 이상, 평점 4.5 이상되는 것만 조회 
# apple, 삼성 등 일부 제품 String으로 삭제 가능하다.
# outube02:10 , if "Apple" in name : continue
# 지금은 첫페이지만 하고 있다 5개 페이지를 해보자.

items = soup.find_all("li",attrs={"class":re.compile("^search-product")})
#print(items[0].find("div",attrs={"class":"name"}).get_text())
#출력된다

#items에 모든 li 상품 리스트들을 담아서 리스트 가지고 있을 것이다.
# 이중에서 해당 태그만 뽑아서 리스트 하나에서 뽑아 쓴다.

for item in items:
    name = item.find("div",attrs={"class":"name"}).get_text()
    print(name)

#위 정보를 String 으로 잘라서 notebookVO List 안에 적재하고 DB에 적재
