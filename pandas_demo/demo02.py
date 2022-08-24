import numpy as np
import pandas as pd

# 创建一个DataFrame
df = pd.DataFrame(data=np.arange(12).reshape(3,4),index=list('abc'),columns=list('wxyz'))
# 显示整个df的结构，相关的信息
df.info()

print('pd默认列优先，numpy默认是行优先')
print(df['w'],type(df['w']))
# 如果是多列,则返回的是子DataFrame
print(df[['w','z']],type(df[['w','z']]))

print('通过iloc采用自然数索引来获取')
print(df.iloc[:,[2,1]])
print(df.iloc[[0,2],[0,2,3]])

print('通过条件来过滤与筛选')
print(df)
print(df[df['y'] > 5])
print('多条件的过滤 | & ~ 运算')
print(df[(df['y']>5) & (df['x']<8)])
print(df[~(df['x']>1)])


