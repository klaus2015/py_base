# 迭代器模式
# 形参和实参问题
# 列表排序
# 函数作用域
# 列表深浅拷贝
# python高阶函数
# 条件表达式
# 跨模块如何条用类的实例方法
# if __name__=="__main__"使用

# 编译实在导包的时候产生的
# pycharm快捷键
# 每种容器的内存图  容器间的互相转换
#判断字典中键是否存在
# *args  **kwargs



# listb = [{"name":"Mcoy","age":18},{"name":"Adam","age":28},
#           {"name":"Talor","age":26},{"name":"Charlie","age":15}]
# def fun01():
#     return listb["age"]
# l = sorted(listb,key=fun01())
# print()
# suits = 'spades diamonds clubs hearts'.split()
# print(suits)
# ranks = [str(n) for n in range(2, 11)] + list("JQKA")
# print(ranks)
# cards = [(rank, suit) for suit in suits for rank in ranks]
# print(cards)
# print(len(cards))
# map01 = [
#             [0, 0, 0, 0],
#             [0, 0, 0, 0],
#             [0, 0, 0, 0],
#             [0, 0, 0, 0],
#         ]
# for line in map01:
#     for item in line:
#         print(item,end=" ")
#     print()
# def fun(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# fun(1,2,3,4,a=5,b=6)
import time
start = time.time()
for item in range(1000000):
    print(item)
t = time.time() - start
print(t)

print(10000000/t)



