"""

在列表中[54, 25, 12, 42, 35, 17]，选出最小值(不使用min)
"""
list01 = [54, 25, 12, 42, 35, 17]
# 假设第一个值为最小值
min_value = list01[0]
# for item in list01:
#     if min_value > item:  # 如果item小于最小值，将item赋值给min_value
#         min_value = item
# print(min_value)


for i in range(1,len(list01)):
    if min_value > list01[i]:
        min_value = list01[i]
print(min_value)
