import numpy as np
import pandas as pd

# df = pd.read_csv("../data/groupby.csv")
# df.info()
# print(df.head(n=4))
#
# print(df['Name'])
# print(df.values, type(df.values))
# print(df.values[:, [1, 3]])


df = pd.read_excel("../data/user.xls", index_col='编号')
# df.info()
print(df.head(n=3))

import random
import xlwt

type = [random.randint(1, 3) for i in range(940)]

df = pd.concat([df, pd.Series(data=type, index=df.index, name="用户类别")], axis=1)
df.to_excel("../data/user_type.xls")
