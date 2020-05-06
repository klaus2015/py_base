"""
regex   re模块 功能函数演示2
生成match对象的函数
"""

import re

s = "今年是2019年,建国70周年"
pattern = r'\d+'

# 返回迭代对象
it = re.finditer(pattern,s)  # 根据正则表达式匹配目标字符串内容
for i in it:
    print(i) # <_sre.SRE_Match object; span=(3, 7), match='2019'>
    print(i.group()) # 2019 获取match对象对应的内容


# 完全匹配一个字符串 --匹配全部内容
it = re.fullmatch(r'\S+',s)
print(it.group()) # 今年是2019年,建国70周年

it = re.fullmatch(r'[,\w]+',s)
print(it.group()) #今年是2019年,建国70周年

# 匹配目标字符串的开始位置
m = re.match(r'\w+',s)
print(m.group()) # 今年是2019年

m = re.match(r'\w+?',s)
print(m.group()) # 今


# 匹配第一处符合正则规则的内容
m = re.search(r'\d+',s)
print(m.group()) # 2019

# compile对象属性

regex = re.compile(r'(ab)cd(?P<pig>ef)')
print(regex.flags) # 32  flags值

print(regex.pattern)  # (ab)cd(?P<pig>ef)  正则表达式

print(regex.groupindex) # {'pig': 2} 捕获组名与组序号的字典

print(regex.groups) # 2  子组数量