import os
dir = '/home/tarena/1905/爬虫1905/文档/'
file_list = os.listdir(dir)
print(file_list)
file_list.sort()
print(file_list)
my_file = dir + '爬虫1-10.md'
for item in file_list:
    filename = dir + item
    print(filename)
    f_obj = open(filename,'rb')
    data = f_obj.read()
    with open(my_file,'ab') as f:
        f.write(data)
f_obj.close()