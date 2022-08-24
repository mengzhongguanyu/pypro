import numpy as np

# 创建np高维矩阵的三种方式
t1= np.arange(12)
# 矩阵支持四则运算（矩阵中每个元素分别进行运算）
print(t1, type(t1))
t1 = t1 + 1
print(t1, type(t1))

# 可以通过reshape修改矩阵的相撞
t1 = t1.reshape(3,1)


