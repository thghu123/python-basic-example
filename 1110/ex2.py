from flask import Flask, jsonify
from flask_cors import CORS #크로스 도메인 이슈 해결
#이제 스프링과 통신, 가장 쉬운 것은 비동기식 통신
from urllib.request import urlopen
import xml.etree.ElementTree as ET
from pandas.core.frame import DataFrame
import requests 

# url = "http://open.ev.or.kr:8080/openapi/services/rest/EvChargerService?serviceKey="
# api_key = "edh68oHntQrWlGu%2B77Bdml97TV9kDdgI07WJt48vzsiU%2FZJxHr3miYl3JLu5jZMidnuQeOoR3pq%2FR13wTO%2F2vQ%3D%3D"
# api_key_decode = requests.utils.unquote(api_key) 
# parameters = {"ServiceKey":api_key_decode, "numOfROws":10, "pageNo":1} 
# spec = requests.get(url, params = parameters)


#파싱용

app = Flask(__name__)
#에러 아직은 코스를 안썻다.
CORS(app)

#URI url = "edh68oHntQrWlGu%2B77Bdml97TV9kDdgI07WJt48vzsiU%2FZJxHr3miYl3JLu5jZMidnuQeOoR3pq%2FR13wTO%2F2vQ%3D%3D"
#url = "edh68oHntQrWlGu%2B77Bdml97TV9kDdgI07WJt48vzsiU%2FZJxHr3miYl3JLu5jZMidnuQeOoR3pq%2FR13wTO%2F2vQ%3D%3D"
#spec = "http://open.ev.or.kr:8080/openapi/services/rest/EvChargerService?serviceKey=edh68oHntQrWlGu%2B77Bdml97TV9kDdgI07WJt48vzsiU%2FZJxHr3miYl3JLu5jZMidnuQeOoR3pq%2FR13wTO%2F2vQ%3D%3D"


spec = "http://open.ev.or.kr:8080/openapi/services/EvCharger/getChargerInfo?ServiceKey=FDp2a3vCnN%2BVvgfwp%2BneIQPvN3zTM7aLpEznSGbkyDN47qXAmtPene0L3A8mgUsbO%2F7pzLR3EX7rdD0%2B6wZe3Q%3D%3D"

#강사님 uri로 등록이 되면 나의 service key로 변경


@app.route("/")
def hello_world():
    str = '''
    <h1>hello world</h1>
    ''' # '''는 주석이자 문자열
    return jsonify(code=str) #what is this??

#이제 spring , flask 동시 다른 포트로 구동 후 비동기식 통신으로 요청


@app.route("/evCar", methods = ['POST'])
def ev_car():
    res = urlopen(spec).read()
    #위에서 인식시킨 파일을 xml로 인식시키기 위해
    xmlDoc = ET.fromstring(res)
    #ET 이제 xml로 바뀌었으니 이제 원하는 태그로 바꿀 수 있다.
    
    #바디 안에 아이템즈를 찾아야한다. 응답메시지 기준
    items = xmlDoc.find('body').find('items')
    #list구조이다.
    rows = []
    for node in items:
        statNm = node.find('statNm').text
        addr = node.find('addr').text
        rows.append({'s_name':statNm, 'addr':addr})
        #제이슨 하나가 객체이다. 통으로 보낼 수 있다.
    df = DataFrame(rows)
    #dataframe의 내용을 json으로 변환한다.
    json = df.to_json(orient = "records")
    return json
    #열일때는 col 컬럼 관련으로 쓴다
