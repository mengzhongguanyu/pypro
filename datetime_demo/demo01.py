# 时间序列简单来说：就是采用时间作为索引来进行相关的操作
import numpy as np
import pandas as pd
from pandas import Series, DataFrame
from datetime import datetime

# 创建构造函数构造日期
date_list = [
    datetime(2016, 9, 1),
    datetime(2016, 9, 10),
    datetime(2017, 9, 1),
    datetime(2016, 9, 20),
    datetime(2017, 10, 1),
]
print('-' * 20, '如何通过日期获取数据', '-' * 20)
# Series索引就是时间序列
s1 = Series(np.random.rand(5), index=date_list)
print(s1.values, s1.index)
print(s1[0])
# 通过日期获取数据
print(s1[datetime(2016, 9, 10)])
# 通过字符串方式获取批量数据
print(s1['2016-09'])

print('-' * 20, '通过data_range生成时间序列', '-' * 20)
date_list = pd.date_range('2016-01-01', periods=30, freq='5h')
s2 = Series(np.random.rand(len(date_list)), index=date_list)
print(s2)

print('-' * 20, '时间序列的采样', '-' * 20)
date_list = pd.date_range(start='2016-01-01',end='2016-12-31')
ss = Series(data=np.random.rand(len(date_list)),index=date_list)
# 采样的前提是index必须为时间序列
print(ss.resample('M').sum()/ss.resample('M').count())
print('-'*100)
print(ss.resample('M').mean())
