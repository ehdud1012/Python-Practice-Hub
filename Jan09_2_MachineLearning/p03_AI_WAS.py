# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
from flask import Flask, jsonify, make_response, request

df = pd.read_csv("C:/KDY/book/자원2023/for AI/datingTestSet.txt", sep="\t", names=["비행기", "게임", "아이스크림", "인기도"])

feature = df[["비행기", "게임", "아이스크림"]].to_numpy()
label = df["인기도"].to_numpy()

mms = MinMaxScaler()
feature = mms.fit_transform(feature) 

knc = KNeighborsClassifier(10)
knc.fit(feature, label)

app = Flask(__name__)

@app.route("/wedding.predict")
def weddingPredict():
    a = float(request.args.get("air"))
    b = float(request.args.get("game"))
    c = float(request.args.get("ice"))

    predictData = np.array([[a, b, c]])
    predictData = mms.transform(predictData)
    result = knc.predict(predictData)
    result = {"result" : result[0]}
    result = jsonify(result)
    result = make_response(result)
    resHeader = {"Access-Control-Allow-Origin" : "*"}
    return result, resHeader


if __name__ == "__main__":
    app.run("0.0.0.0", 9898, debug=True)
