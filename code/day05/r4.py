# list01 = [54, 25, 12, 42, 35, 17]
# list02 = []
# for item in list01:
#     if item > 30:
#         list02.append(item)
# print(list02)


#
# number = 0
# count = 0
# while count < 5:
#     count += 1
#     number01 = int(input("请输入数字： "))
#     if number < number01:
#         number = number01
# print(number)


# 我的代码
# list01 = []
# number01 = 0
# count = 0
# while count < 5:
#     count += 1
#     number = int(input("请输入一个数字： "))
#     list01.append(number)
#     for item in list01:
#         if item > number01:
#             number01 = item
#
# print(number01)


# 老师代码
# max_value = 0
# for item in range(5):
#     number = int(input(("请输入第%d个数字") % (item+1)))
#     if max_value < number:
#         max_value = number
# print(max_value)


# list01 = [54, 25, 12, 80, 35, 17]
# max_value = list01[0]
# for item in range(1,len(list01)):
#     if list01[item] > max_value:
#         max_value = list01[item]
# print(max_value)


#练习4
list01 = [9, 25, 12, 8]
# for item in list01:
#     if item > 10:
#         list01.remove(item) #删除原理，后一个覆盖前一个
# print(list01) # [9. 12, 8]


# 3 2 1 0  从后往前删除可以避免上面的问题
for i in range(len(list01)-1,-1,-1):
    if list01[i] > 10:
        list01.remove(list01[i])
print(list01) # [9, 8]



# 有问题
# -4 -3 -2 -1
# for i in range(-1,-len(list01),-1):
#     if list01[i] > 10:
#         list01.remove(list01[i])
# print(list01) # [9, 8]