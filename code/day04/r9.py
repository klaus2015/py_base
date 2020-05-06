"""
一个小球从１００ｍ的高度落下
    　　每次弹回原高度的一半．
    　　计算：总共弹起来多少次（最小弹起高度0.01ｍ）．
            总共走了多少米


"""

# 弹1次，走了100 +50
# 弹2次，走了100+50 50+ 25
# 弹3次，走了100 +50+50+ 25+25+ 12.5
# 弹4次，走了100 +50+50 +25+25+ 12.5+12.5+ 6.25
# 弹4次，走了100 +50+50 +25+25+ 12.5+12.5+ 6.25+ 6.25 + 3.125
count = 0
# 直接加上起始距离
sum_hight = 100
hight = 100
# 弹起前高度 大于最小弹起高度
#while hight > 0.01:
# 弹起来的高度 大于最小弹起高度
while hight / 2 > 0.01:
    count += 1
    hight *= 0.5 #弹起高度的变化
    sum_hight += hight*2  # 弹起落下算一次循环，第一次下落不做考虑
    print("第%d次弹起%f的高度" %(count, hight)) #
print("总共弹起%d次" % count)
print(sum_hight)


# 如何判断代码是否正确，通过代码第26行的结果判断出来第14次高度已经小于0.01M，
# 然后又从新考虑while的成立条件，后再 hight /2
# 打印出每次的循环结果，依次和判断条件做对比，验证代码是否正确；