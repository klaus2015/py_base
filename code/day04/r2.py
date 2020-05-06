"""
珠峰高8848.43
一张纸厚度0.00001
折多少次能超过珠峰

"""
#  老师的代码
mount_everest_hight = 8848.43
paper = 0.00001
count = 0
# while paper < 8848.43:
#     count += 1
#     paper *=  2
#     print(paper)
# print(count)

# 有问题，注意与下面代码的区分
while True:
    count += 1
    paper *= 2
    if paper > 8848.43:
        print(paper)
        break
print(count)

#我自己的思路，
# mount_everest_hight = 8848.43
# paper = 0.00001
# count = 0
# while True:
#     count += 1
#     paper *= 2
#     if paper > 8848.43:
#         break
#     print(paper)
# print(count)