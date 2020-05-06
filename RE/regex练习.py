"""
regex   re模块 功能函数演示1
"""

import re

# 目标字符串
s = "Alex:1994,Sunny:1996"
pattern = r"\w+:\d+" # 正则表达式

# re模块直接调用findall

l = re.findall(pattern,s) # 匹配到的内容列表,如果正则表达式有子组则只能获取到子组对应的内容
print(l) # ['Alex:1994', 'Sunny:1996']


# pattern = r"(\w+):(\d+)" # 只能获取到子组对应的内容
# l = re.findall(pattern,s)
# print(l) # [('Alex', '1994'), ('Sunny', '1996')]


# complie对象调用findall

regex = re.compile(pattern) # 这里正则表达式已经确定
l = regex.findall(s) # --参数就一个目标参数
print(l) # ['Alex:1994', 'Sunny:1996']

regex = re.compile(pattern)
l = regex.findall(s,0,12) # Alex:1994,Su  只能匹配到一处 即截取目标字符串
print(l) # ['Alex:1994']