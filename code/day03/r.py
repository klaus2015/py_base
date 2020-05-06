sex = input(("请输入男女： "))
if sex == "男":
    print("你好男士")
if sex == "女":
    print("你好女士")
else:
    print("性别未知")
# 第二行和第六行没有互斥性
#
# if sex == "男":
#     print("你好男士")
# elif sex == "女":
#     print("你好女士")
# else:
#     print("性别未知")

# price = int(input("请输入商品单价："))
# count = int(input("请输入数量： "))
# money = int(input("请输入金额： "))
# result = money - count * price
# if result >= 0:
#     print("你的找零", result)
#     print("请收好你的钱，欢迎下次光临！")
# else:
#     print("对不起，你付款金额不足！")
# 方法1   4个if没有互斥性，及时满足条件出现了，后续程序依然会继续执行完
# quarter = input("请输入一个季度： ")
# if quarter == "春":
#     mounths = "1月、2月、3月"
# if quarter == "夏":
#     mounths = "4月、5月、6月"
# if quarter == "秋":
#     mounths = "7月、8月、9月"
# if quarter == "冬":
#     mounths = "10月、11月、12月"
# print(quarter + "对应的月份是：" + mounths)


# 方法2  想比方法1，优点：如果前面天剑满足，后续条件不在判断！
# quarter = input("请输入一个季度： ")
# if quater == "春":
#     mounths = "1月、2月、3月"
# elif quarter == "夏":
#     mounths = "4月、5月、6月"
# elif quarter == "秋":
#     mounths = "7月、8月、9月"
# else:
#     mounths = "10月、11月、12月"
# print(quarter + "对应的月份是：" + mounths)