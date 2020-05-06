"""
    练习1:定义计算四位整数，每位相加和的函数.
    测试："1234"   "5428"
"""
def each_unit_sum(number):
    result = number % 10
    result += number // 10 % 10
    result += number // 100 % 10
    result += number // 1000
    return result

re = each_unit_sum(1400)
print(re)
