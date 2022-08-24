import numpy as np
import pandas as pd

# 先创建一个Series(列)
ss = pd.Series(data=list('ABC'),index=list('abc'),name='title')
print(ss,ss.index,ss.name)
print(ss.values,type(ss.values))
print('-'*100)
# 创建一个DataFrame
df = pd.DataFrame(data=np.arange(12).reshape(3,4),index=list('abc'),columns=list('wxyz'))
# 显示整个df的结构，相关的列信息
df.info()
print(df,type(df))
print(df.columns,df.values,type(df.values))
print('获取某一列,个打印values的数据类型')
print(df['y'],type(df['y']))
