"""
flags 扩展功能演示
"""
import re
s = """Hello
北京
"""

# 只能匹配ASCII编码 --美式键盘字母

regex = re.compile(r'\w+')
l = regex.findall(s)
print(l) # ['Hello', '北京']

regex = re.compile(r'\w+',flags=re.A)
l = regex.findall(s)
print(l) #--['Hello']


# 不区分大小写 ---验证码不区分大小写
regex = re.compile(r'[a-z]+')
l = regex.findall(s)
print(l) # ['ello']

regex = re.compile(r'[a-z]+',flags=re.I)
l = regex.findall(s)
print(l) # ['Hello']

# 使 . 可以匹配换行

regex = re.compile(r'.+')
l = regex.findall(s)
print(l) # ['Hello', '北京']

regex = re.compile(r'.+',flags=re.S)
l = regex.findall(s)
print(l) # ['Hello\n北京\n']

# 使 ^ $可以匹配每一行的开头结尾位置

regex = re.compile(r'^北京')
l = regex.findall(s)
print(l) # []

regex = re.compile(r'^北京',flags=re.M) # 每一个的开头
l = regex.findall(s)
print(l) # ['北京']

regex = re.compile(r'Hello$',flags=re.M) # 每一个的结尾
l = regex.findall(s)
print(l) # ['Hello']

# 给正则分行注释

pattern = r"""\w+ # hello
\s+ # 匹配换行
\w+ # 北京
"""
regex = re.compile(pattern,flags=re.X)
l = regex.findall(s)
print(l) # ['Hello\n北京']

# 4. 使用多个flag
# 方法:使用按位或连接
# e.g. : flags = re.I | re.A
