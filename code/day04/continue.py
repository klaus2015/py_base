"""
累加10~50之间个位不是2/5/9的整数

"""

sum_value = 0
# 我的代码
for item in range(10, 51):
    if (item % 10) % 2 == 0 or (item % 10) % 5 == 0 or (item % 10) % 9 == 0:# 忽略了2和5的倍数
        continue
    sum_value += item
print(sum_value)


#老师代码
# for item in range(10, 51):
#     unit = item % 10
#     if unit == 2 or unit == 5 or unit == 9:
#         continue
#     sum_value += item
# print(sum_value)