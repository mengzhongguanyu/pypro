# 可视化的高级参数设置
import numpy as np
import matplotlib.pyplot as plt

# 设置微软雅黑，支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
print('-' * 20, '层叠柱状图的可视化操作', '-' * 20)
data1 = np.random.randint(20, 50, size=5)
data2 = np.random.randint(20, 50, size=5)
# 模拟x轴的坐标值
x = np.arange(1, 6)
print(data1, data2)
plt.bar(x, data1, label='A')
plt.bar(x, data2, bottom=data1, label='B')
# label要显示则调用此方法
plt.legend()
plt.show()

print('-' * 20, '层叠柱状图的可视化操作2', '-' * 20)
data1 = np.random.randint(20, 50, size=5)

for a, b in zip(x, data1):
    plt.text(a, b + 0.5, b, ha='center', fontsize=12)

data2 = np.random.randint(20, 50, size=5)

for a, b in zip(x, data2):
    plt.text(a + 0.3, b + 0.5, b, ha='center', fontsize=12)

x = np.arange(1, 6)
plt.bar(x, data1, width=0.3, label='A')
plt.bar(x + 0.3, data2, width=0.3, label='B')
plt.legend()
plt.show()
