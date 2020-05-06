"""
获取两个变量，互换并交换结果

"""
# # 获取第一个变量
# a = input("请输入变量一： ")
# # 获取第二个变量
# b = input("请输入第二个变量： ")
# # 交换变量
# # temp = data01
# # data01 = data02
# # data02 = temp
#
# a, b = b, a
# # 输出结果
# print("第一个变量结果是" + a)
# print("第二个变量结果是" + b)
# print(1.5)
# print(5 // 2)
# print(5 / 2)
# print(27 % 10)

# """
# 获取商品总价钱
# """
# # 录入商品单价
# price = float(input("请输入商品单价： "))
# #录入商品数量
# count = int(input("请输入商品数量： "))
# # 显示付款数
# money = int(input("请输入付了多少钱： "))
#
# result = money - price * count
# print("应找回：",result,"元钱")

# min = float(input("获取分钟： "))
# hour = float(input("获取小时： "))
# day = int(input("获取天数： "))
# second = min * 60 + hour ** 60 + day * 24 * 3600
# print("总秒数是", second)

# 获取两数
# ounce = int(input("请输入两数： "))
# result01 = ounce // 16
# result02 = ounce % 16
# print("结果是",result01,"斤",result02,"两")

# 获取加速度
# distance = float(input("请输入距离： "))
# initial_speed = float(input("请输入初速度： "))
# time = float(input("请输入时间： "))
# accelerated_speed = ((distance - initial_speed * time) * 2) / time **2
# print("加速度是： ",accelerated_speed)

# # 获取一个整数
# number = int(input("请输入四位整数： "))
# unit01 = number % 10
# unit02 = number //10 % 10
# unit03 = number //10 % 10
# unit04 = number // 1000
# result = unit01 + unit02 + unit03 + unit04
# print(result)

# 方法二

# result = number % 10
# result += number //10 % 10
# result += number //100 % 10
# result += number // 1000
# print(result)


# 判断年份是否为闰年
# 闰年：年份能被4整除，但是不能被100整除
# 或者能被400整除
year = int(input("请输入年份： "))
result = (year % 4 == 0 and year % 100 != 0) or year % 400 == 0
print("是否是闰年：", result)
