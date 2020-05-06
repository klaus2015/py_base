"""
在控制台中录入一个字符串，判断是否为回文．
  判断规则:正向与反向相同．
  　　　上海自来水来自海上
"""

string = input("请输入一个字符串： ")
positive_sequence = string[:]
reverse_sequence = string[::-1]
# 判断是否是回文
if positive_sequence == reverse_sequence:
    print("输入的字符串回文")

else:
    print("输入符合要求")