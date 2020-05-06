# sum_value = 0
# for item in range(1, 101):
#     sum_value += item
# print(sum)
#
# for item in range(2, 100, 2):
#     sum_value += item
# print(sum_value)





import  random
score = 0
# for item in range(3):
#     num01 = random.randint(1, 11)
#     num02 = random.randint(1, 11)
#     print("请输入", str(num01), "+", str(num02), "的和： ")
#     sum01 = int(input("输入结果： "))
#     if sum01 == (num01+num02):
#         score += 10
# print(score)


for item in range(3):
    num01 = random.randint(1, 11)
    num02 = random.randint(1, 11)
    print("请输入", str(num01), "+", str(num02), "的和： ")
    sum01 = int(input("输入结果： "))
    if sum01 == (num01+num02):
        score += 10
print(score)



# count = 0
# score = 0
# while count < 3:
#     count += 1
#     num01 = random.randint(1, 11)
#     num02 = random.randint(1, 11)
#     print("请输入", num01, "+", num02, "的和： ")
#     if int(input("请输入数字：")) == num01 + num02
#         score += 10



#number = int(input("请输入一个数字： "))

# 我的脑残代码
# if number % 2 == 0:
#     if number % 5 == 0:
#         if number % 7 == 0:
#             print("是素数")
# else:
#     print("不是素数")

# for item in range(2, number):
#     if number % item == 0:
#         print("不是素数")
#         break
# else:
#     print("素数")
