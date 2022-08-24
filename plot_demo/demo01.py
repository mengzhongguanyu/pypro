import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# # github中加载远程的数据集
# tips = sns.load_dataset("tips")
# print(tips.type(tips))
# tips.info()
# print(tips.head(n=3))
# # DataFrame保存csv格式
# tips.to_csv("../data/tips.csv",index_label='row_id')
# 设置微软雅黑，支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
tips = pd.read_csv('../data/tips.csv')
tips.info()
# 如果是相关性,则建议采用散点图
plt.scatter(tips['total_bill'],tips['tip'])
# 对x,y输入标题
plt.xlabel('消费金额')
plt.ylabel('小费金额')
# 所有可视化都需要调用show函数
plt.show()