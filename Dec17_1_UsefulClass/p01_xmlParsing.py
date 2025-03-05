# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from xml.etree.ElementTree import fromstring

# 파이썬에서하는 HTTP 통신
#   https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1111061500
#   http    -  HTTPConnection
#   https   -  HTTPSConnection
  
hc = HTTPSConnection("www.kma.go.kr") # (주소:포트) 까지만
hc.request("GET", "/wid/queryDFSRSS.jsp?zone=1111061500") # 요청방식(GET/POST), 남은주소 (맨 앞 / 주의)

# 응답
res = hc.getresponse() 
resBody = res.read()
# print(resBody)
# print(resBody.decode()) # 한글 처리해서 내용 확인 / 파싱할 땐 위에 껄로

#-----------------------------------------------------------------------------

# XML 파싱
#   Java   : XML 파싱 기능 X -> kxml.jar 사용
#   Python : XML 파싱 기능 있음

weatherData = fromstring(resBody)
datas = weatherData.iter("data") # <data></data> 들 / 여러개 찾을때는 iter

for w in datas:
    print(w.find("temp").text) # <temp></temp> / 하나 나오는거 찾을 떄는 find
    print(w.find("temp").text)
hc.close()