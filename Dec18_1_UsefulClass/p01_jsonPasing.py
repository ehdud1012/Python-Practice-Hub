# -*- coding:utf-8 -*-
from http.client import HTTPSConnection
from json import loads
# https://api.openweathermap.org/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr

hc = HTTPSConnection("api.openweathermap.org")
hc.request("GET", "/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")

resBody = hc.getresponse() .read()

# JSON 파싱
#   Java   : 없어서 json-simple.jar
#   Python : 있음

# JSON - JS형태로 데이터 표현
# JS의 배열 : [1,2,3]
#       Python의 list
# JS의 객체 : {name : "이름", ...}
#       Python의 dict

weatherData = loads(resBody)    # JSON -> Python의 collection (list, dict ..)
# print(type(weatherData))        # dict

print("날씨 : %s" % weatherData["weather"][0]["description"])
print("온도 : %s" % weatherData["main"]["temp"])
print("체감온도 : %s" % weatherData["main"]["feels_like"])

hc.close()