import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

tips = sns.load_dataset("tips")
#
# tips.info()
#
# print(tips.head(30))
#
# tips.to_csv("../data/tips.csv", index_label="row_id")

plt.rcParams['font.sans-serif'] = ['SimHei']
tips = pd.read_csv("../data/tips.csv")

time = tips['time'].value_counts()

plt.pie(labels=time.index, x=time.values, autopct='%4.2f%%')
plt.show()
