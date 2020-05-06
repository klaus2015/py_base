file_obj = open("text",'r')

# while True:
#     data = file_obj.read(10)
#     if not data:
#         break
#     print(data)

# data = file_obj.readline(1)
# print(data)
# data = file_obj.readline()
# print(data)

# data = file_obj.readlines(1)
# print(data)
for i in file_obj:
    print(i,end="")

file_obj.close()