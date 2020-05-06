"""
regex   re模块 功能函数演示2
match 对象属性演示
"""

import re

pattern = r'(ab)cd(?P<pig>ef)'

regex = re.compile(pattern)
obj = regex.search('abcdefghi') # obj --match对象

#属性变量
print(obj.pos) # 目标字符串开始位置  --0
print(obj.endpos) # 目标字符串结束位置 -- 9

# oj = regex.search('abcdefghi',0,8)
# print(oj.pos) # 目标字符串开始位置 --0
# print(oj.endpos)# 8

print(obj.re) # 正则表达式 re.compile('(ab)cd(?P<pig>ef)')
print(obj.string) # abcdefghi

print(obj.lastgroup) # 最后一组的名称 pig
print(obj.lastindex) # 最后一组的序号 2
print('=======================================')
# 属性方法
print(obj.span()) # 获取匹配内容的起止位置 (0, 6)
print(obj.start()) # 获取匹配内容的开始位置 0
print(obj.end()) # 获取匹配内容的结束位置 6

print(obj.groupdict()) # 获取捕获组字典,组名为键,对应内容为值 {'pig': 'ef'}
print(obj.groups()) # 获取子组对应内容的元组 ('ab', 'ef')
print(obj.group()) #获取match对象匹配内容 默认为0表示获取整个match对象内容 --abcdef
print(obj.group('pig')) # 如果是序列号或者组名则表示获取对应子组内容 --ef
print(obj.group(1)) # ab
print(obj.group(2)) # ef