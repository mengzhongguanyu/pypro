import numpy as np

t1 = np.arange(12).reshape(3,4)
# 获取某个元素且赋值
t1[0,0] = 100
print(t1)
print('选择连续的行和列')
print(t1[0:2,1:])
print('选择连续的行与不连续的列')
print(t1[1:,[1,3]])
print('选择不连续的行与列')
# 【0,1】【2,3】
print(t1[[0,2],[1,3]])
print('正确选择不连续的行与列(需要两步)')
t2 = t1[:,[1,3]]
print(t2[[0,2],:])
print('逻辑元素的方式筛选元素')
# 返回t1同等尺寸的布尔矩阵
print(t1 > 8)
# 矩阵方括号中支持布尔值
print(t1[True])
# 布尔值可以是1个，也可以和行数相等，也可以每个元素一个
# 第二行就会被过滤掉
print(t1[[True,False,True]])
# 保留布尔值对应位置的元素
print(t1[t1>8])
