# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 15:26:16 2021

@author: rick
"""
import pandas as pd               # 資料處理套件
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False
school = pd.read_csv("school.csv")
year = [None] * len(school["年份"])
plt.style.use("ggplot")
plt.plot(school["年份"], school["人次"],c = "r") 