import random
random_num = random.randint(1,100)

# while True:
#     guess_num = int(input("请输入一个数字： "))
#     if guess_num == random_num:
#         print("恭喜你答对了！")
#         break
#     elif guess_num > random_num:
#         print("大了，大了")
#     else:
#         print("小了小了")


count = 0
# while True:
#     count += 1
#     guess_num = int(input("请输入一个数字： "))
#     if guess_num == random_num:
#         print("恭喜你答对了！")
#         print(count)
#         break
#     elif guess_num > random_num:
#         print("大了，大了")
#     else:
#         print("小了小了")

# 我自己的思路
# while True:
#     if count < 3:
#         count += 1
#         guess_num = int(input("请输入一个数字： "))
#         if guess_num == random_num:
#             print("恭喜你答对了！")
#             break
#         elif guess_num > random_num:
#             print("大了，大了")
#         else:
#             print("小了小了")
#     else:
#         print("游戏失败")
#         break

while count < 3:
    count += 1
    guess_num = int(input("请输入一个数字： "))
    if guess_num == random_num:
        print("恭喜你答对了！")
        break
    elif guess_num > random_num:
        print("大了，大了")
    else:
        print("小了小了")

else:
    print("游戏失败")