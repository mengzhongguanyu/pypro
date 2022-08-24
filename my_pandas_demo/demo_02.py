import numpy as np
import pandas as pd

df:pd.DataFrame = pd.DataFrame(data=np.arange(12).reshape(3, 4), index=list('abc'), columns=list('wxyz'))
df.info()
print(df['w'], type(df['w']))
print(df[['w', 'z']], type(df[['w', 'z']]))

print(df.iloc[:, [2,1]])
print(df.iloc[[0,2], [0,2,3]])

print(df)
print(df[df['y'] >5])

print(df[(df['y'] > 5) & (df['x'] < 8)])

