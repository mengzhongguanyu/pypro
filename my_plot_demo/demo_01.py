import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

# tips = sns.load_dataset("tips")
#
# tips.info()
#
# print(tips.head(30))
#
# tips.to_csv("../data/tips.csv", index_label="row_id")

plt.rcParams['font.sans-serif'] = ['SimHei']
tips = pd.read_csv("../data/tips.csv")

print("消费预消费的金额")
# 如果是相关性 采用散点图
plt.scatter(tips['total_bill'], tips['tip'])
plt.xlabel('消费')
plt.ylabel('小费')
plt.show()