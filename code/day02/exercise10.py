"""
获取总秒数，计算几小时零几分钟零几秒

"""
# 获取总秒数
total_second = int(input("输入总秒数： "))
# 秒数结果
senond = total_second % 60
# 分钟结果
minute = total_second // 60 % 60
# 小时结果
hour = total_second // 3600
print("小时、分钟、秒数分别是：", hour, minute, senond)

