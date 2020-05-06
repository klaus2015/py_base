import os
dir = '/home/tarena/1905/爬虫1905/文档/'
file_list = os.listdir(dir)
for item in file_list:
    if '0' in item:
        print(item)

