# 可视化的高级参数设置
import numpy as np
import matplotlib.pyplot as plt

# 设置微软雅黑，支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
print('-' * 20, '年份与GDP的折线图', '-' * 20)
years = [str(year) + "年" for year in range(2010, 2020)]
# print(years)
gdp = np.random.randint(300, 1000, size=10)
# print(gdp)
# plt.plot(years, gdp, color="green", marker='*',linestyle='--')
plt.plot(years, gdp, 'r--*')
plt.show()

print('-' * 20, '饼图与保存图片', '-' * 20)

data = {
    '南京': (60, '#7199cf'),
    '上海': (45, '#4fc4aa'),
    '北京': (120, '#ffff10'),
}
# 设置绘图片的信息
cities = data.keys()
values = [x[0] for x in data.values()]
colors = [x[1] for x in data.values()]
plt.pie(x=values, explode=[0.2, 0.05, 0.05], labels=data.keys(), colors=colors, autopct='%4.2f%%')
plt.show()
