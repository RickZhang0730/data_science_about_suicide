import pandas as pd
import matplotlib.pyplot as plt 

plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei'] 
plt.rcParams['axes.unicode_minus'] = False

#死亡率和死因資料統計(折線圖)
# =============================================================================
# plt.style.use('bmh')
# data = pd.read_csv('104青年主要死亡原因.csv')
# df = data[data['死亡原因(合計)']!='所有死亡原因']
# plt.plot(df['死亡率%(合計)'], df['死亡原因(合計)'],c = "r")
# plt.xlabel("死亡率%(合計)", fontweight = "bold")                # 設定x軸標題及粗體
# plt.ylabel("死亡原因(合計)", fontweight = "bold")    # 設定y軸標題及粗體
# plt.title("104年", fontsize = 15, fontweight = "bold", y = 1.1) 
# 
# =============================================================================

#各年度自殺比較(折線圖)
# =============================================================================
# plt.style.use('bmh')
# data_104 = pd.read_csv('104青年主要死亡原因.csv')
# data_104_rate = data_104['死亡率%(合計)'].loc[2]
# 
# data_105 = pd.read_csv('105青年主要死亡原因.csv')
# data_105_rate = data_105['死亡率%(合計)'].loc[2]
# 
# data_106 = pd.read_csv('106青年主要死亡原因.csv')
# data_106_rate = data_106['死亡率%(合計)'].loc[2]
# 
# data_107 = pd.read_csv('107青年主要死亡原因.csv')
# data_107_rate = data_107['死亡率%(合計)'].loc[2]
# 
# data_108 = pd.read_csv('108青年主要死亡原因.csv')
# data_108_rate = data_108['死亡率%(合計)'].loc[2]
# 
# final = {"年份":['104','105','106','107','108'],
#          "死亡率%":[data_104_rate,data_105_rate,data_106_rate,data_107_rate,data_108_rate]}
# plt.plot(final['年份'], final['死亡率%'],c = "r")
# plt.xlabel("年份", fontweight = "bold")                # 設定x軸標題及粗體
# plt.ylabel("死亡率%", fontweight = "bold")    # 設定y軸標題及粗體
# plt.title("各年度自殺率死亡比較", fontsize = 15, fontweight = "bold", y = 1) 
# =============================================================================

#自殺原因統計(圓餅圖)
# =============================================================================
# data_pie = pd.read_csv('108年自殺原因統計.csv')
# plt.pie(data_pie['比例數%(合計)'],labels= data_pie['自殺原因'], autopct='%1.1f%%')
# =============================================================================

#可以得到順位i的資料
#print(data.loc[i])