import re

content = 'http://weibo.com/comment/KEraCN'
re1 = re.match('http.*?comment/(.*?)',content)
re2 = re.match('http.*?comment/(.*)',content)
print(re1.group(1))
print(re2.group(1))