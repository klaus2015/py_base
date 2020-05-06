"""
求100-999的所有水仙花数
"""
list_sum_result = []
for item in list(range(100, 1000)):
    if item == (item % 10)**3 + ((item//10) % 10)**3 + (item // 100)**3:
        list_sum_result.append(item)
        print(item)
# 打印水仙花数的和
print(sum(list_sum_result))