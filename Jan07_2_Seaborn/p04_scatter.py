# -*- coding:utf-8 -*-
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import seaborn as sns

fontFile = "C:/Windows/Fonts/malgun.ttf"
fontName = fm.FontProperties(fname=fontFile, size=10).get_name() 
plt.rc("font", family=fontName)
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_csv("C:/KDY/example/subway/cspf.csv", names=["년", "월", "노선", "역", "찍고탄", "그냥탄", "찍고내린", "그냥내린"])
df["그냥"] = df["그냥탄"] + df["그냥내린"]

# sns.scatterplot(x="찍고탄", y="찍고내린", data=df, palette="coolwarm")
# sns.scatterplot(x="찍고탄", y="찍고내린", data=df, hue="노선", palette="coolwarm")
sns.scatterplot(x="찍고탄", y="찍고내린", data=df, size="그냥", palette="coolwarm")
plt.show()