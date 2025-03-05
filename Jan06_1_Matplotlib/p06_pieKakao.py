from enum import auto
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import pandas as pd

plt.rc("font", family=fm.FontProperties(fname="C:/Windows/Fonts/malgun.ttf", size=10).get_name())
plt.rcParams["axes.unicode_minus"] = False 

df = pd.read_csv("C:/KDY/kakaoChatNameCountResult.txt", sep="\t", names=["이름", "횟수"])
df = df[df["횟수"] != 1]

df = df.sort_values(by="횟수", ascending=False)

name = df["이름"].to_numpy()
count = df["횟수"].to_numpy()

plt.pie(count, labels=name, autopct="%.1f%%")
plt.show()