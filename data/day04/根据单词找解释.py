f = open("dict.txt","r")
word = input("请输入单词: ")

# 缺陷 ,a列中abc找不到,但是还是一直遍历到低
for i in f:
    if word == i.split(" ")[0]:
        print(i)
        break

else:
    print("单词没有找到")


