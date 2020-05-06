"""
练习一
"""
# month = int(input("请输入月份："))
#
# if month < 1 or month > 12:
#     print("输入有误")
# elif month == 2:
#     print("２８天")
# elif month in (4,6,9,11):  # 利用元组的成员判定
#     print("３０天")
# else:
#     print("３１天")


# 方法二
# month = int(input("请输入月份："))
#
# if month < 1 or month > 12:
#     print("输入有误")
# else:
#     day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
#     print(day_of_month[month-1])

# 求几月几号是一年的第几天
# 索引求结果
day_of_month = (31,28,31,30,31,30,31,31,30,31,30,31)
month = int(input("请输入月份： "))
day = int(input("请输入几号： "))
# total_day = 0
# for i in range(month-1):
#     result01 += day_of_month[i]
# total_day += day
# print(total_day)

# 切片求结果
total_day = sum(day_of_month[:month-1])
total_day += day
print(total_day)
