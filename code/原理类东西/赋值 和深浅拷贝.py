import copy
# 字典/列表有copy()方法,则拷贝后的内存地址与原来地址不同
# a = [1,2]
# c = copy.copy(a)
# print(id(a))   #140016416583624
#
# print(id(c))    #140016416585800
# 数字/字符串/元组 没有copy()方法的数据类型,浅拷贝等于赋值
a = (1,2,3)
b = copy.copy(a)
print(id(a))   # 140380390233792
print(id(b))   #140380390233792