"""
给定本期大奖结果[6,12,13,14,20,28,9]
利用循环计算产生多少注会中大奖
"""
import random
# 彩票大奖
lottery_result = [6,12,13,14,20,28,9]
# 创建自己买的彩票
# 随机生成6个红球
count = 0
while True:
    count += 1
    my_lottery = []
    for i in range(6):
        number_red_ball = random.randint(1, 33)
        if number_red_ball not in my_lottery: # 如果产生的红球不在列表中，就加入列表
            my_lottery.append(number_red_ball)
    # 将列表中红球按从小到大排序
    my_lottery.sort()
    #随机生成一个蓝球
    number_blue_ball = random.randint(1, 16)
    # 将蓝球加入列表中，输出彩票结果
    my_lottery.append(number_blue_ball)
    if my_lottery == lottery_result:
        print("恭喜你，中特等奖！！！")
        print(count)
        break
