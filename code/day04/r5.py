# a = 1
# b = 2
# str01 = "请输入%d + %d" % (a, b)
# print(str01)


string = input("输入一个字符串： ")
print(string[0])
print(string[-1])
print(string[-3])
print(string[:2])
print(string[::-1])
if len(string) % 2 == 1:
    print(string[1:3])
