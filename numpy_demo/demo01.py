import numpy
import numpy as np

print('创建np高维矩阵的一种方式')
t1: numpy.ndarray = np.arange(12)
# 矩阵支持四则运算 (矩阵中每个元素分别进行运算)
t1 = t1 + 1
print(t1, type(t1), t1.shape)
l = [1, 2, 3, 4, 5]
# 必须nd.array与list区别
# l = l + 1
print(l, type(l))
# 可以通过reshape修改矩阵的形状
t1 = t1.reshape(3, 4)
print(t1, type(t1), t1.shape)

print('创建np高维矩阵的二种方式')
# 可以把list转化为ndarray
data = [[1, 2, 3.14, 4],
        [True, 6, 7, None]]
print(data, type(data))
# 创建ndarray时支持各种类型
t2 = np.array(data)
print(t2, type(t2), t2.shape)

print('创建np高维矩阵的三种方式')
t3 = np.random.random(size=[3, 4])
print(t3, type(t3), t3.shape)
t3 = np.random.randint(1, 100, size=(3, 4))
print(t3, type(t3), t3.shape)
t3 = np.random.normal(loc=10, size=[3, 4])
print(t3, type(t3), t3.shape)
