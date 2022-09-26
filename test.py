import pandas as pd
import matplotlib.pyplot as plt
medicine = pd.read_csv('medicine.csv')
ml=medicine.loc[3]
mll=ml.iloc[1:9]
mll=mll.astype(int)
recall = pd.read_csv('recall.csv')
re=recall.loc[0]
re=re.iloc[1:14]
re=re.astype(int)
school = pd.read_csv('school.csv')
sh=school.loc[0]
sh=sh.iloc[1:14]
mll.plot(title='憂鬱藥使用人數(30歲以下)')
re.plot.barh(title='各年齡自殺通報占比')
sh.plot(title='校園自殺通報數')