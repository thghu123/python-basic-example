#원래 __init__은 그자체이기에 evCar만 해도된다

from flask import Flask

#cross domain errer 방지
from flask_cors import CORS

#공공 데이터에게 요청해서 데이터 가져오자
#다른 곳에 있는 openAPI와 연결하려는 준비 
from urllib.request import urlopen

#xml로 제공한다 , 파서 필요
import xml.etree.ElementTree as ET
#pandas 사용
import pandas as PD
from pandas.core.frame import DataFrame

app = Flask(__name__)
#cross domain 방지
CORS(app)

spec = "http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?ServiceKey=FDp2a3vCnN%2BVvgfwp%2BneIQPvN3zTM7aLpEznSGbkyDN47qXAmtPene0L3A8mgUsbO%2F7pzLR3EX7rdD0%2B6wZe3Q%3D%3D"
#매핑
app.route("/evCar",methods = ['POST'])#post로 주고싶은 경우
#함수 정의
def ev_car():
    #openapi 연결 후 문자열로 받기
    res = urlopen(spec).read() #url 들어가서 한번에 읽어온다
    xmlDoc = ET.fromstring(res) #문자열로 된 xml을 xml 객체로 만들겠다. -> 파싱 xml객체 -> 특정 element tag로 구분해서 가져올 수 있다.
                                #문자열에서 특정 요소들만 찾고 싶다. 문자열에서 요소만 찾기는 쉽지 않다. body 찾고 items 찾고 가능하도록
    items = xmlDoc.find('body').find('items')

    #items안에 있는 item을 원한다. 안의 주소가 필요하다 우리가 필요한 item들을 의미부여된 JSON형태로 한곳에 모아둬야한다.
    rows = []#한곳에 담아야하니까 리스트를 선언한다
    for i in items: #넣는다
        statNm = i.find("statNm").text#얻으려는 변수와 동명으로 지정
        chgerType = i.find("chgerType").test #충전 타입
        addr = i.find("addr").text
        #이렇게 받아둔 걸 JSON타입으로 만들어야한다

        rows.append({"s_name":statNm, "type":chgerType, "addr":addr})   #하나의 자원 주입
    df = DataFrame(rows) #json 형태로 모여진 애들이 table 형태로 자리 잡힌다. 맨위 행은 s_name, type, addr이다
    #addr만 필요하다면 따로 DataFrame을 만들어도된다

    df2 = DataFrame({"city":df['addr'].str.split(" ",expand=True)[0]}) #문자열로 만들고 자름 + 덧붙여라 
    #주소만 모아서 dataFrame 만들어진다, 시군만 필요하다 (서울 특별시. 경기도 등등 나온다.)
    #서울 특별시의 전기 충전소가 몇개있는가? 쓸 데 없는 데이터 잘라낸다.




    





