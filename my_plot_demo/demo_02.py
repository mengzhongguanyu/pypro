import pandas as pd

import matplotlib.pyplot as plt


plt.rcParams['font.sans-serif'] = ['SimHei']
tips = pd.read_csv("../data/tips.csv")

print("性别与小费的相关性")
print(tips['sex'] == 'Male')

male_mean = tips[tips['sex'] == 'Male']['tip'].mean()
female_mean = tips[tips['sex'] == 'Female']['tip'].mean()

plt.bar(['male', 'female'], [male_mean, female_mean], width=0.6)
plt.title("柱状图")
plt.show()

print("-"*100)
print("采用分组实现")
ss = tips.groupby(by='day')['total_bill'].sum()
print(ss, type(ss))

plt.bar(ss.index, ss.values)
plt.title("柱状图")
plt.show()




