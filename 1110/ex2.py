from flask import Flask, jsonify
from flask_cors import CORS #크로스 도메인 이슈 해결
#이제 스프링과 통신, 가장 쉬운 것은 비동기식 통신

app = Flask(__name__)
#에러 아직은 코스를 안썻다.
CORS(app)

@app.route("/")
def hello_world():
    str = '''
    <h1>hello world</h1>
    ''' # '''는 주석이자 문자열
    return jsonify(code=str) #what is this??

#이제 spring , flask 동시 다른 포트로 구동 후 비동기식 통신으로 요청

