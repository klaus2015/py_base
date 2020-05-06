"""
使用正则表达式匹配内容,切割目标字符串
"""

import re

# 目标字符串
s = "Alex:1994,Sunny:1996"

# 按照正则表达式匹配内容切割字符串
l = re.split(r'[:,]',s)
print(l) # ['Alex', '1994', 'Sunny', '1996']

# 替换目标字符串
l = re.sub(r':','-',s) # 默认全部替换
print(l) # Alex-1994,Sunny-1996

l = re.sub(r':','-',s,1) # 只替换一处
print(l) # Alex-1994,Sunny:1996

l = re.subn(r':','-',s) # 替换后的字符串和替换了几处
print(l) # ('Alex-1994,Sunny-1996', 2)--替换2处