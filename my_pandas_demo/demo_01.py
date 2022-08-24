import numpy as np
import pandas as pd


ss:pd.Series = pd.Series(data=list('ABC'), index=list("acb"), name='title')
print(ss, ss.index, ss.values)

print('-'*100)
df = pd.DataFrame(data=np.arange(12).reshape((3,4)), index=list('abc'), columns=list('wxyz'))
df.info()
print(df, type(df))
print(df.columns, df.values)

print(df['y'], type(df["y"]))


