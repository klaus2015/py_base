"""
    群讨论：is  与 == 的区别
"""
# 只有数值型和字符串型的情况下，a is b才为True，当a和b是tuple，list，dict或set型时，a is b为False。
# a = (1,2,3)
# b = (1,2,3)
# print(a is b)
# print(a == b)
# def fun07(a, b, *args, c, **kwargs, d):
#     print(a)
#     print(b)
#     print(args)
#     print(c)
#     print(d)
#     print(kwargs)
#
# fun07(1,2,3,4,5,c=6,d=7,f=1,g=2,h=3)
#
# print(1,2,"哈哈",sep=" ----",end=" ")
# print(1,2,3)
# list01 = []
# list01.insert()


# def fun07(*args,**kwargs):
#     print(args)   # (1, 2, 3)
#     print(kwargs)
# fun07(1,2,3,a=100,b=5008)  #{'a': 100, 'b': 5008}



