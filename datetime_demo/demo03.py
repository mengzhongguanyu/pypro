# 时间序列简单来说：就是采用时间作为索引来进行相关的操作
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
data = pd.read_csv("../data/bike.csv")
# 首先把datetime转化为日期类型
data['datetime'] = pd.to_datetime(data['datetime'])
data.info()
# 把时间序列设置为索引
data.set_index('datetime',inplace=True)
print(data.head(n=3))
print('-'*20,'对日期的采样,统计每天的骑行数据','-'*20)
d_bike = data.resample('d')['count'].mean()
print(d_bike,type(d_bike))
# 先创建新的day,hour
data['day'] = data.index.day
data['hour'] = data.index.hour
print(data,type(data))
print('通过分组统计每小时的骑行记录')
h_bike = data.groupby(by='hour')['count'].sum()
print(h_bike,type(h_bike))
# 采用线性图,查看每小时的骑行数据
plt.plot(h_bike.index,h_bike.values,'r--*')
# 自定义刻度坐标值
plt.xticks(range(h_bike.size),[i+1 for i in range(h_bike.size)])
plt.savefig('./h_bike.jpg')
plt.show()