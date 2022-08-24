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
# 按月进行采样,获取每月总租赁数据
ss = data.resample('M')['count'].sum()
data_2011 = ss['2011']
data_2012 = ss['2012']
print(data_2011,data_2012)
# 生成月份的x轴数据
attr = [f'{i}月' for i in range(1,13)]
v1 = data_2011.values
v2 = data_2012.values
# 通过柱状图显示相关的租赁数据
plt.bar(attr,v1,label='2011月份租赁')
plt.bar(attr,v2,bottom=v1,label='2012月份租赁')
plt.xlabel('月份')
plt.ylabel('租赁总量')
plt.legend()
plt.show()