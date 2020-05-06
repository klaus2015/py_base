"""
随机产生一注彩票[6个红球１个蓝球]
"""
import random
# 创建彩票列表
list_lottery = []
# 随机生成6个红球
while len(list_lottery) < 6:
    number_red_ball = random.randint(1, 33)
    if number_red_ball not in list_lottery: # 如果产生的红球不在列表中，就加入列表
        list_lottery.append(number_red_ball)
# 将列表中红球按从小到大排序
list_lottery.sort()
#随机生成一个蓝球
number_blue_ball = random.randint(1, 16)
# 将蓝球加入列表中，输出彩票结果
list_lottery.append(number_blue_ball)
print(list_lottery)



