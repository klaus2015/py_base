list01 = ["香蕉", "苹果","哈密瓜"]
list02 = ["可乐","牛奶"]
list03 = [r + c for r in list01 for c in list02]
print(list03)