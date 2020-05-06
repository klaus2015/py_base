# print(ord("a"))
# str01 = chr(97)
# print(str01)

# str1 = input("请输入一个字符串： ")
# for item in str1:
#     print(ord(item))


while True:
    str_code = input("请输入一个编码值： ")
    if str_code == " ":
        break
    int_code = int(str_code)
    print(chr(int_code))
