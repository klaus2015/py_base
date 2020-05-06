count = 1
list_lottery = []  # 彩票列表
# 我的代码
while count < 6:   # 随机产生6个红球

    number_red = int(input(("请输入第%d个红球号码: ") % count ))
    if 1 <= number_red <= 33:
        if number_red not in list_lottery:
            list_lottery.append(number_red)
            count += 1
        else:
            print("号码已经重复。")

    else:
        print("号码不在范围内。")


list_lottery.sort() # 红球从小到大排序
while True:         # 循环产生蓝球
    number_blue = int(input("请输入蓝球号码： "))
    if 16 < number_blue or number_blue < 1:
        print("号码不在范围内，请重新输入： ")
    else:
        list_lottery.append(number_blue)
        break
print(("你购买的彩票为%s") % list_lottery)



# 老师的产生红球的代码

while count < 6:   # 随机产生6个红球

    number_red = int(input(("请输入第%d个红球号码: ") % count ))
    if number > 33 or number < 1:
        print("号码不在范围内。")
    elif number_red in list_lottery :
        print("号码已重复。")

    else:
        list_lottery.append(number_red)
        count += 1


