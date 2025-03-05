# -*- coding:utf-8 -*-

# 분석/AI 결과를 어떻게 써먹을건가
# -> Back-end프로그래밍해서 결과를 JSON으로 만들어내면
# => 써먹기 가능

# Back-end
#   Java : Spring / SpringBoot
#   JavaScript : Node.js
#   Python : Django / Flask

# 제대로 웹개발하려면 Spring/SpringBoot
# 결과를 단순히 JSON으로만 만들기 위함이라면 Flask

# Django 
#   - Spring급
#   - 제대로 웹 개발하려면 사용

# Flask  
#   - Servlet급 (Node.js)
#   - 요청-응답만
#   - 실무 점유율이 높음
#   설치 - pip install flask

from flask import Flask, jsonify, make_response, request

# Flask 객체
app = Flask(__name__)

# Spring 느낌
# 이 주소로 요청 날리면
@app.route("/")
def test():
    # 여기서 결과를 Json으로 만들기
    return "asdf"  # 응답

# 파라메터값 넣어서 요청 / 응답
@app.route("/param.test")
def paramTest():
    x = request.args.get("x")
    y = request.args.get("y")
    return x+y  # 그냥 붙여서 나옴 계산하려면 숫자로 바꿔야

# JSON으로 응답
@app.route("/json.res.test")
def jsonResTest():
    a = int(request.args.get("a"))  # 숫자로 바꾸기
    b = int(request.args.get("b"))
    c = a + b
    # JS객체 : {} = Python dict
    # JS배열 : [] = Python list
    # JSON :  JS객체 + JS배열

    # 1. 일단 Python dict + list로
    d = {"a" : a, "b" : b, "sum" : c}
    # 2. jsonify : Python의 dict + list -> JSON
    #       loads : JSON -> Python의 dict + list
    e = jsonify(d)
    # 3. 응답
    resBody = make_response(e)
    return resBody

@app.route("/cda.test")
def crossDomainAJAXTest():
    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    c = a + b
    resBody = make_response(jsonify({"a" : a, "b" : b, "sum" : c}))
    # 응답헤더 설정
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return resBody, resHeader

# 파이썬의 메인
if __name__ == "__main__":
    app.run(
        # "192.168.0.56" # 접속할 주소 (이 주소를 제외한 모든 주소 안됨 ex-localhost, 127.0.0.0, ...)  
        "0.0.0.0",       # 모든 주소 가능
        9898,            # 포트번호
        debug=True       # 콘솔에 접속 기록 찍/안찍
    )
