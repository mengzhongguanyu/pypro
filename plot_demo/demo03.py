# 如何获取数据源
import pandas as pd
import matplotlib.pyplot as plt

# 设置微软雅黑，支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
tips = pd.read_csv('../data/tips.csv')
tips.info()
# value_counts(必须作用于某列)：对某一列进行分组然后求和
time = tips['time'].value_counts()
print(time,type(time))
# 创建饼图
plt.pie(labels=time.index,x=time.values,autopct='%4.2f%%')
plt.show()

# 新建列，存储相关的数据(例如：小费百分比)
tips['percent_tip'] = round(tips['tip']/(tips['total_bill']+tips['tip'],2))
tips.to_csv("../data/tip2.csv",index=False)