# num1 = int(input("请输入一个数字： "))
# num2 = int(input("请再输入一个数字： "))
# operator = input("请输入一个运算符： ")
# if operator == "+":
#     result = num1 + num2
# elif operator == "-":
#     result = num1 - num2
# elif operator == "*":
#     result = num1 * num2
#
# elif operator == "/":
#     result = num1 / num2
# else:
#     result = "请输入正确的运算符！"
# print("结果是：" + str(result))


#练习3
number_one = int(input("请输入一个数字： "))
number_two = int(input("请输入一个数字： "))
number_three = int(input("请输入一个数字： "))
number_four = int(input("请输入一个数字： "))
result = number_one
if result < number_two:
    result = number_two
if result < number_three:
    result = number_three
if result < number_four:
    result = number_four
print("最大的是",result)

