import matplotlib.pyplot as mp
import numpy as np

# 随机生成一组数据
n = 300
# 172:	期望值
# 10:	标准差
# n:	数字生成数量
height = np.random.normal(175, 5, n)
weight = np.random.normal(70, 7, n)

mp.figure('Persons', facecolor='lightgray')
mp.title('Persons',fontsize=18)
mp.xlabel('height',fontsize=14)
mp.ylabel('weight',fontsize=14)
mp.grid(linestyle=':')
d = (height-175)**2 + (weight-70)**2
mp.scatter(
    height,weight,marker='o',s=70,label ='persons',c=d,cmap='jet')
mp.legend()
mp.show()

# # 随机生成一组数据
# n = 300
# height = np.random.normal(175, 5, n)
# weight = np.random.normal(70, 7, n)
#
# mp.figure('Persons', facecolor='lightgray')
# mp.title('Persons', fontsize=18)
# mp.xlabel('height', fontsize=14)
# mp.ylabel('weight', fontsize=14)
# mp.grid(linestyle=':')
# d = (height - 175) ** 2 + (weight - 70)**2
# mp.scatter(
#     height, weight, marker='o', s=70,
#     label='persons', c=d, cmap='jet')
# mp.legend()
# mp.show()