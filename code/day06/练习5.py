"""
将1970年到2050年中的闰年，存入列表
"""
list_leap_year = []
for item in range(1970, 2051):
    if item % 4 == 0 and item % 100 != 0 or item % 400 == 0:
        list_leap_year.append(item)
print(list_leap_year)

# 列表推导式
list_leap_year01 = [item for item in range(1970, 2051) if item % 4 == 0
                  and item % 100 != 0 or item % 400 == 0 ]

print(list_leap_year01)

