import numpy as np

print('常见属性')
t1 = np.arange(12).reshape(3,4)
print(t1,type(t1),t1.shape)
print('矩阵元素的数量:', t1.size)
print(f'元素类型{t1.dtype},所占的空间大小:{t1.itemsize}个字节')
t1 = t1.astype(np.float64)
print(f'元素类型{t1.dtype},所占的空间大小:{t1.itemsize}个字节')
print('矩阵的升降维')
# (1000,10,10) ==> (1000,100)
t1 = np.arange(12).reshape(3,4)
# 矩阵运算: 就是矩阵中每个元素分别进行运算
t2 = t1 + 1
print(t2)
# 对二维矩阵进行降维操作, order='F' 则是列优先
t3 = t1.flatten(order='C')
t3 = t3 + 1
t3 = t3.reshape(3,4)
print(t3)
print('矩阵的四则运算操作')
# 让t2形状与t1完全相同
t2 = t1
print(t2)
t3 = t2 * t1
print(t3)
print('矩阵尺寸可以不同,但是必须 (?,1) , (1,?)')
t2 = np.arange(4).reshape(1,4)
print(t2)
# t2中的4个元素，与t1中的每一行4个元素分别进行运算
print(t1 + t2)
# t2中的3个元素，与t1中的每一列3个元素分别进行运算
t2 = np.arange(3).reshape(3,1)
print(t2)
print(t1 * t2)