# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:19:58 2021

@author: rick
"""
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt   # 資料視覺化套件

work = pd.read_csv("suicide.csv")

plt.figure(figsize=(10,10))    # 顯示圖框架大小

labels = work["自殺方式(通報)"]    # 製作圓餅圖的類別標籤
size = work["總計"]   # 製作圓餅圖的數值來源

plt.pie(size,                           # 數值
        labels = labels,                # 標籤
        autopct = "%1.1f%%",            # 將數值百分比並留到小數點一位
        pctdistance = 0.85,              # 數字距圓心的距離
        textprops = {"fontsize" : 14},  # 文字大小
        shadow = False)                  # 設定陰影

 
plt.axis('equal')                        # 使圓餅圖比例相等
plt.title("自殺通報(總計)", {"fontsize" : 20})  # 設定標題及其文字大小
plt.legend(loc = "best")                 # 設定圖例及其位置為最佳

plt.savefig("work_Pie.png", bbox_inches='tight') #存檔，第二個參數表示把圖表外多餘的空間刪除
plt.show()