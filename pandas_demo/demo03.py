import numpy as np
import pandas as pd
import random
import xlwt

print('加载本地的csv格式文件')
df = pd.read_csv("../data/groupby.csv")
df.info() # 显示相关的信息
print(df.head(n=3))
# 获取某一列的数据
print(df['Name'])
print(df.values,type(df.values))
# 通过ndarray API也可以直接获取values
print(df.values[:,[1,3]])

print('加载本地的excel格式文件')
df = pd.read_excel("../data/user.xls",index_col='编号')
df.info()
print(df.head(n=3))
# 随机生成940个1~3之间的数
type = [random.randint(1,3) for _ in range(940)]
# df追加列
df = pd.concat([df,pd.Series(data=type,index=df.index,name='用户类别')],axis=1)
df.to_excel("../data/user_type.xls")
