from PIL import Image
import numpy as np

# 加载图片
data = Image.open("../data/phone.jpg")
# RGB 红绿蓝
print(data,type(data))
# 图片转化矩阵的格式
im = np.array(data)
# 颜色值 [0~255]
print(im.shape,im.dtype)
# 原始图的矩阵值
print(im)
b = [255,255,255] - im
print('运算之后的结果')
print(b)
new_im = Image.fromarray(b.astype(np.uint8))
new_im.save("../data/phone2.jpg")