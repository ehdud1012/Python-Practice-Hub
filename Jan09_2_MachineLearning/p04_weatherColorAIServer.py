# -*- coding:utf-8 -*-
from datetime import datetime
from oracledb import connect, init_oracle_client
import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, jsonify, make_response, request
from http.client import HTTPConnection
from json import loads
import cv2

# 학습데이터 불러다 학습 시키기
#   - 밖 : 처음 한번만 되니 -> 업데이트 불가
#   - 안 : 매번 데이터를 불러서 학습 -> 시간 ↑
#   -> 업데이트도 가능하고 시간도 너무 오래 안걸리는 방법 ?
#       1. 매일 새벽에만 한 번     : 밖에다 두고, 리눅스 서버에 스케쥴러  -> 가장 괜찮은 방법이지만, 현재 할 수 없으니
#       2. 매일 첫 요청에만 한 번  : 이걸로 진행

# 매번 할 필요가 없는 애들 -> 함수 안에서는 global 사용
init_oracle_client(lib_dir="C:/KDY/lib/instantClient/instantclient_23_4")
mms = MinMaxScaler()
knc = KNeighborsClassifier(10)
app = Flask(__name__)
weathers = None
day = -1
# 데이터 학습시키기
def trainAI():
    global mms, knc, weathers
    # DB연결해서 데이터 불러오기
    con = connect("ehdud1012/1012@192.168.0.55:1521/xe") 
    sql = "SELECT * FROM pooh_weather_color"
    df = pd.read_sql(sql, con)
    con.close()
    # 한글 인코딩
    weathers = list(df["PWC_DESCRIPTION"].unique())
    df["PWC_DESCRIPTION"] = df["PWC_DESCRIPTION"].apply(lambda w:weathers.index(w))
    # 학습 시키기
    feature = df[["PWC_TEMP", "PWC_FEEL_TEMP", "PWC_HUMIDITY", "PWC_DESCRIPTION"]].to_numpy()
    label = df["PWC_COLOR"]
    feature = mms.fit_transform(feature) 
    knc.fit(feature, label)

# 현재 날씨 불러오기
def getCurWeather():
    global weathers
    hc = HTTPConnection("api.openweathermap.org")
    hc.request("GET","/data/2.5/weather?q=seoul&appid=baff8f3c6cbc28a4024e336599de28c4&units=metric&lang=kr")
    rb = hc.getresponse().read()
    hc.close()
    weatherData = loads(rb)
    temp = weatherData["main"]["temp"]
    feel = weatherData["main"]["feels_like"]
    humi = weatherData["main"]["humidity"]
    desc = weatherData["weather"][0]["description"]
    # 한글 인코딩
    try:
        desc = weathers.index(desc) 
    except:
        desc = -1
    return temp, feel, humi, desc

@app.route("/weather.color.predict")
def weatherColorPredict():
    global mms, knc, day
    today = datetime.today().day
    if day != today:
        trainAI()
        day = today
        
    temp, feel, humi, desc = getCurWeather()    # 현재 날씨는 매번 필요
    predictData = np.array([[temp, feel, humi, desc]])
    predictData = mms.transform(predictData)
    result = knc.predict(predictData)[0]
    result = {"color" : result}
    result = jsonify(result)
    return make_response(result), {"Access-Control-Allow-Origin" : "*"}

if __name__ == "__main__":
    app.run("0.0.0.0", 9898, debug=True)