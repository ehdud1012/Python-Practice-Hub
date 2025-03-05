# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads

from bs4 import BeautifulSoup
# BD분석/AI훈련용 데이터 구축
#   1) 직접 (몸으로) 
#       ex) 아침마다 지하철 임산부석 확인 
#   2) 웹 데이터
#       XML/JSON 파싱
#       만약 데이터가 없으면..?
#           HTML파싱 = webCrawling (웹 페이지에서 데이터 긁어모으기)
#               XML/JSON - openApI 데이터 편히 가져가하고 만든
#               HTML     
#               - 웹 사이트 디자인 언어 
#               - 법적문제 유의 (근데 사이트 들어가면 보이는뎅 ..)
#               - 파싱 난이도 ↑
#               - 막아놓은 사이트 다수 (보이긴 하지만 웹 크롤링은 막아놓은)
#               - 동적으로 생성되는 HTML (클릭하면 나오는)
#                   selenium - 브라우저 열어서 버튼 클릭하는 메크로 -> 브라우저 내용 크롤링  
#   3) 어디서 파일 구해와서 
#       

#  webCrawling
#   XML/JSON/HTML 파싱 통칭 (작게 구분하면 HTML 파싱)
#   HTML 파싱 
#       - 기본 내장 X -> 남꺼 가져와 ~ (BeautifulSoup.py)
#           중앙처리시스템
#               Java    - gradle/maven
#               Node.js - npm 
#               Python  - pip
#           인터넷 직접 들어가서 .py 받아오거나 / pip 사용
#           pip
#               cmd -> pip install 이름 (pip install bs4)
#           만약 자바에서 HTML 파싱 하고 싶으면 JSoup.jar 추가 후 사용 (사용법 동일)

# 카페 사용 https://sd-beanmouse.duckdns.org/

hc = HTTPSConnection("sd-beanmouse.duckdns.org")
hc.request("GET", "/")
resBody = hc.getresponse() .read()
#                  (읽어온 html, 내장 html 파서 이름, 인코딩 언어)
snsData = BeautifulSoup(resBody, "html.parser", from_encoding="utf-8")

# sns 내용 부분 가져오기
# snsData.select("CSS 선택자") 문법은 이게 끝
txt = snsData.select(".txtTd")
for i in txt:
    print(i.text)


hc.close()