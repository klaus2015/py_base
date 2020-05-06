"""
在控制台中获取一个整数作为边长．

"""
length = int(input("请输入边长： "))
string = "*"
space = ' '
print(string * length-2)
for item in range(length):
    print(string + space * (length - 2) + string)

print(string * length)
