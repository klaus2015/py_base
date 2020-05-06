"""
    身份运算符
"""

a = 800
b = 1000
# id函数，可以获取变量存储的对象地址。
print(id(a)) # 140122519510320
print(id(b)) # 140122488349136
# flase
print(a is b)  # is 的本质就是通过ｉｄ函数进行判断的

c = a
print(id(c)) # 140122519510320
print(c is a) # True

d = 1000
print(id(d)) # 140122488349136
print(d is b) # True
print(id(1000))
