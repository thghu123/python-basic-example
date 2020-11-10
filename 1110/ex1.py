# from flask import Flask

# app = Flask(__name__) #상수 인자 input to flask  

# @app.route("/test")
# def test():
#     return "hello flask"
# "hello flask" ouput success

from flask import Flask, g
#g, global object ,서블릿의 servletContext와 같은 객체
#저장해두면 application이라는 큰 영역(전체 영역)에 저장해 쓰던 서블릿 컨텍스트
#flask도 유사한 g가 존재

app = Flask(__name__)#무조건 입력

#어떤 request든 요청 이전에 수행
@app.before_request
def before_request():
    g.msg = 'g에 저장된 값'
    

#요청하면 수행하는 함수
@app.route("/test2")
def test2():
    return "반갑습니다 "+getattr(g,'msg')
#g에 저장된 속성을 얻돼 속성 이름은 msg

#http://127.0.0.1:5000/test2 수행시 잘나온다
