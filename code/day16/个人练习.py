#1python中字符串可以用单引号括起来，也可以用双引号，这两种方式是等价的,单引号中可以包含双引号,双引号中可以包含单引号,
# 两种表示方法,省去转义引号的麻烦
#三引号的形式用来输入多行文本，也就是说在三引号之间输入的内容将被原样保留，
# 之中的单号和双引号不用转义，其中的不可见字符比如\n和\t都会被保留，这样的好处是你可以替换一些多行的文本
#2 ---1  [1]
#3 *args 将位置实参合并成元组,**kwargs将关键字实参合并成字典
#4
# def get_square(a):
#     return a ** 2
# list01 = [1,2,3,4,5]
# list02 = list(map(get_square,list01))
#
# print(list02)
# list03 = [item for item in list02 if item > 10]
# print(list03)
#5
# import datetime
# print(datetime.date.)

#6
# listb = [{"name":"Mcoy","age":18},{"name":"Adam","age":28},
#          {"name":"Talor","age":26},{"name":"Charlie","age":15}]
# print(len(listb))
# for r in range(len(listb)-1):
#     for c in range(r+1,len(listb)):
#         if listb[r]["age"] > listb[c]["age"]:
#             listb[r],listb[c] = listb[c],listb[r]
#
# print(listb)
# 7
#8
A0 = {"a":1,"b":2,"c":3,"d":4,"e":5}
A1 = range(0,10)
A2 = []
A3 = [1,2,3,4,5]
A4 = [1,2,3,4,5]
A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}
A6 = [[0,0],[1,1],[2,4],[3,9],[4,16],[5,25],[6,36],[7,49],[8,64],[9,81]]
#9
f(2)---[0,1]
f(3,[3,2,1])-----[3,2,1,0,1,2]
f(3)------[0,1,2]

"""11 __new__ 通常用于控制生成一个新实例的过程。它是类级别的方法
_init__ 通常用于初始化一个新实例，控制这个初始化的过程，
比如添加一些属性发生在类实例被创建完以后。它是实例级别的方法
"""
#12 使用模块class MyClass(object):
#     def __init__(self):
#         self.a = 1
#
# s_myclass = MyClass()
# from mysingleton import s_myclass
#
# s_myclass.a
# 13
#161. match（）函数只检测re是不是在string的开始位置匹配，也就是说match（）
# 只有在0位置匹配成功的话才有返回，如果不是开始位置匹配成功的话，match()就返回none
# search()会扫描整个string查找匹配
