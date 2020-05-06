# state = None
# number = int(input("请输入一个整数： "))
# if number % 2 :
#     state = "奇数"
# else:
#     state = "偶数"
# print(state)

# state = "奇数" if int(input("请输入整数： ")) % 2 else "偶数"
# print(state)

year = int(input("请输入年份："))
result = year % 4 == 0 and year % 100 != 0 or year % 400 == 0
if result:
    day = 29
else:
    day = 28
print(day)
代码简单，但是可读性差  能被4整除但是不能被100整除，或者可以被400整除
day = 29 if not year % 4 and year % 100 or not year % 400 else 28

day = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
result = year % 4
print(result)
year = 2000
result =  year % 4
print(result)