"""
    　　　2. 编写一个文件拷贝程序，从终端输入一个文件，
　　　　　将文件保存在当前目录下

        * 文件类型不确定（可是文本文件，可能是二进制文件）
"""
# while True:
#     file_obj = input("请输入文件名称: ")
#     try:
#         f = open(file_obj,"rb")
#         break
#
#     except FileNotFoundError as f:
#         print(e)
#
# while True:
#     data = f.read()
#     if not data:
#         break
#     f_obj = open("tt.jpg","wb")
#     f_obj.write(data)
#     f_obj.close()



file_obj = input("请输入文件名称: ")
try:
    f = open(file_obj,"rb")


except FileNotFoundError as f:
    print(f)
else:
    f_obj = open("tt.jpg", "wb")
    while True:
        data = f.read(1024)
        if not data:
            break
        f_obj.write(data)
    f.close()
    f_obj.close()