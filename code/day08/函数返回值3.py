# 定义函数，根据年月，计算有多少天，考虑闰年，闰年29，平年28

def is_leap_year(year):
    """
    判断是否是闰年
    :param year: 需要判断的年份
    :return: 返回闰年二月天数
    """
    return  year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_day_for_month(month, year):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31


print(get_day_for_month(2, 2000))
