# def each_unit_sum(num):
#     """
#     计算四位整数每位相加和
#     :param num: 输入的四位数
#     :return: 返回每位相加和
#     """
#
#     result = num % 10
#
#     result += num // 10 % 10
#
#     result += num // 100 % 10
#
#     result += num // 1000
#     return result
#
# number = int(input("请输入四位整数： "))
# r = each_unit_sum(number)
# print(("输入的%d的每位相加结果是：%d") % (number, r))

# def calculate_jin_liang(weight_liang):
# # get_weight_for_jin
#     """
#     根据两数，计算出是几斤几两
#     :param weight_liang: 传入的两数
#     :return: 返回几斤几两
#     """
#
#     jin = weight_liang // 16
#     liang = weight_liang % 16
#     return (jin, liang)
#
# weight_liang = int(input("请输入两："))
#
# result = calculate_jin_liang()
#
# print(("结果是%d斤%d两") % (result[0],result[1]))






# 根据成绩计算等级的函数
def get_level_for_score(score):
    """
    根据成绩计算等级优秀 良好 及格 不及格

    :param score: 输入的成绩
    :return: 返回等级
    """

    if score > 100 or score < 0:
        greade = "输入有误"
    elif 90 <= score:
        grade = "优秀"
    elif 80 <= score:
        grade = "良好"
    elif 60 <= score:
        grade = "及格"
    else:
       grade = "不及格"
    return grade


result = get_level_for_score(100)
print(result)
print()

# 方法2 更好
def get_level_for_score(score):
    """
    根据成绩计算等级优秀 良好 及格 不及格

    :param score: 输入的成绩
    :return: 返回等级
    """

    if score > 100 or score < 0:
        return "输入有误"
    if 90 <= score:
        return "优秀"
    if 80 <= score:
        return "良好"
    if 60 <= score:
        return "及格"
    return "不及格"
