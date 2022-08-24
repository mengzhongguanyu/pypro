# 如何获取数据源
import pandas as pd
import matplotlib.pyplot as plt

# 设置微软雅黑，支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
tips = pd.read_csv('../data/tips.csv')
tips.info()
print('性别与小费的相关性可视化')
male_mean = tips[tips['sex'] == 'Male']['tip'].mean()
female_mean = tips[tips['sex'] == 'Female']['tip'].mean()
# 采用bar柱状图显示金额
plt.bar(['male','female'],[male_mean,female_mean],width=0.5,color='#ff0000')
plt.title('bar柱状图可视化案例')
plt.show()
# 采用分组的方式，实现就餐日期与消费金额的关联性
ss = tips.groupby(by='day')['total_bill'].sum()
print(ss,type(ss))
# 可视化中Series可以和可视化组件进行无缝转化
plt.bar(ss.index,ss.values,color='#00ff00')
plt.title('就餐日期与消费的柱状图')
plt.show()