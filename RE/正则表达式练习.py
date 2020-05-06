"""
匹配一个邮箱格式字符串
匹配一个密码 8-12位数字字母下划线构成
匹配一个数字 正数 负数 整数 小数 分数1/2 百分数45%
匹配一段文字中以大写字母开头的单词,iPython不算,H-Base算
"""
import re
s = 'today is 55 a good.com day ,我的邮箱是: 598467866@qq.com'
r = re.findall(r'\w+@\w+\.com',s)
print(r)

s = 'Zxm_153113'
r = re.findall(r'\w{8,12}',s)
print(r)

s = "Over at the iPython new Aquatics Centre, " \
       "B-ritain's star diver Tom Daley is."

r = re.findall(r'\b[A-Z][-_a-zA-Z]*',s)
print(r)

r = re.findall(r'-?\d+/?\.?\d*%?','12 -3 3.5 -5.45 42% 1/3')
print(r)

# 匹配身份证号
r = re.search(r'\d+','41078119900415311X').group()
print(r) # 41078119900415311 --排他性差

r = re.search(r'\d{18}','410781199004153113').group()
print(r) # 410781199004153113 --排他性差

r = re.search(r'\d{17}(\d|X)','41078119900415311X').group()
print(r)  # 41078119900415311X  --排他性相对较好