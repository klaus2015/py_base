# 列表到字符串
# list_temp = []
# for item in range(10):
#     list_temp.append(str(item))
# # result = "".join(list_temp) #0123456789
# result = "*".join(list_temp)  # 0*1*2*3*4*5*6*7*8*9
# print(result)


# list_temp = []
# while True:
#     string = input("请输入字符串： ")
#     if string == "":
#         break
#     list_temp.append(string)
#
# result = "".join(list_temp)
# print(result)
# print(type(result))

# 字符串到列表

# star01 = "张无忌-赵敏-周芷若"
# list_result = star01.split("-")
# print(list_result)

# 英文单词反转

star01 = "how are you"
list01 = star01.split(" ")
print(list01) # ['how', 'are', 'you']
list_result = list01[::-1]
print(list_result) # ['you', 'are', 'how']
str_result = " ".join(list_result)
print(str_result)   # you are how

