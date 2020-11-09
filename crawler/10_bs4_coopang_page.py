import requests
import re
from bs4 import BeautifulSoup
#여기서 쿠팡과 달리 다나와는 전체 노트북 정보가 안나온다. 이를 셀러리움으로 해야한다.

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

for i in range(1,2):
    print("현재 페이지:",i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(i)

    res = requests.get(url, headers = headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text,"lxml")
    # 지금은 첫페이지만 하고 있다 5개 페이지를 해보자.

    items = soup.find_all("li",attrs={"class":re.compile("^search-product")})



    for item in items:
        link = item.find("a",attrs = {"class":"search-product-link"})["href"]
        name = item.find("div",attrs={"class":"name"}).get_text()
        print(name)
        print("바로가기 : {}".format("www.coupang.com"+link))
        print("----------------------------------------------------")
    


