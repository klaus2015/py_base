import re

s = "老齐: qtx@tedu.cn"

print(re.findall('\w+@\w+.cn', s))

r = re.findall('ab', 'abcdefab')
print(r)

r = re.findall('com|cn', 'https//www.baidu.com.cn')
print(r)

r = re.findall('张.丰','张三丰,张四丰,张五丰')
print(r)

r = re.findall('张.丰','张三丰,张四丰,张\n丰,')
print(r)

r = re.findall('[aeiou]',"How are you!")
print(r)

r = re.findall('[aeiou]',"aou!")
print(r)

r = re.findall('[0-9]',"1998")
print(r)

r = re.findall('[_#0-9a-z]','1998#Abs') # 混合书写,一般区间表达写在后面,单个字符放在前面
print(r)

r = re.findall('[^_#0-9a-z]','1998#Abs') # ^ 取反
print(r)

r = re.findall('^tom','tom,hello')
print(r) # ['tom']

r = re.findall('^tom','hi,tom')
print(r) # []

r = re.findall('tom$','hello,tom')
print(r) # ['tom']

r = re.findall('^tom,hello$','tom,hello')  # 完全匹配 如果两者同时出现,则中间的部分必须匹配整个目标字符串的全部内容。
print(r)  #--['tom,hello']

r = re.findall('he*','we,hello,hee,h')
print(r) # ['he', 'hee', 'h']

r = re.findall('de*','abcdefg,dee')
print(r) # ['de', 'dee']

r = re.findall('[a-zA-Z]*','How are you')
print(r) # ['How', '', 'are', '', 'you', '']

r = re.findall('[0-9]*','T am 18')
print(r)  # ['', '', '', '', '', '18', '']

r = re.findall('[A-Z][a-z]*','How are you,Fine Tom, I am fine')
print(r) # ['How', 'Fine', 'Tom']['How', 'Fine', 'Tom', 'I']

r = re.findall('[A-Z][a-z]+','How are you,Fine Tom, I am fine') # I 未找到
print(r) # ['How', 'Fine', 'Tom']

r = re.findall('ab?','abbbbb,abcde,a') # ? 操作的是 b,a后面b出现0次或一次
print(r)  # ['ab', 'ab', 'a']

r = re.findall('[0-9]+|-[0-9]+','167 -28 29 -8')  # 我的
print(r)  # ['167', '-28', '29', '-8']

r = re.findall('-?[0-9]+','167 -28 29 -8')  # 老师的
print(r)  # ['167', '-28', '29', '-8']

r = re.findall('.*[a-zA-Z0-9].*','port-9 Errtr #404# %@STD') # 我的
print(r)  # ['port-9 Errtr #404# %@STD']

r = re.findall('[^ ]+','port-9 Errtr #404# %@STD') # 老师的
print(r)  # ['port-9', 'Errtr', '#404#', '%@STD']

r = re.findall('ab{3}','abbbbbbbbbbb')
print(r) # ['abbb']

r = re.findall('1[0-9]{10}','张三:13846523198')
print(r) # ['13846523198']

r = re.findall('1[0-9]{10}','张三:13846523198,李四:15449871235')
print(r) # ['13846523198', '15449871235']

r = re.findall('张.{3}','张三丰丰')
print(r)

r = re.findall('ab{2,4}','abbbb')
print(r) # ['abbbb']  --贪婪模式,匹配更多的

r = re.findall('[1-9][0-9]{5,10}','qq:1259296994')
print(r)

r = re.findall('\d{1,5}','Mysql:3306, http:80')
print(r)  # ['3306', '80']

r = re.findall('\D+','Mysql:3306, http:80')
print(r) # ['Mysql:', ', http:']

r = re.findall('\w+','server_port:8000 你好呀') # 普通utf-8字符都可以匹配出来
print(r) # ['server_port', '8000', '你好呀']

r = re.findall('\w+\s+\w+','hello    world!')
print(r)  # ['hello    world'] # 匹配到的是整体

r = re.findall('\S+','Hello    world!')  # 空字符指 空格 \r \n \t \v \f 字符-----print()打印出来看不见的字符即空字符
print(r)  # ['Hello', 'world!']  # 匹配到的是两个单词 --非空字符

r = re.findall('\Ahello','hello   world')
print(r) # ['hello']

r = re.findall('world\Z','hello   world')
print(r) # ['world']

r = re.findall('is','This is a test')
print(r) # ['is', 'is']---This is

r = re.findall(r'\bis\b','This is a  test') # \b 能被转义成退格,所有正确写法 \\b,\\bis\\b-----另写法r'\bis\b'
print(r)  # ['is'] --is

r = re.findall(r'\Bis\b','This is a  test')
print(r)  # ['is']  --This

r = re.findall(r'\b\d+\b','123 65 Num007')
print(r) # ['123', '65']

r = re.findall(r'\d+\b','123 65 Num007')
print(r) # ['123', '65', '007']

r = re.findall('\d\*\*\d+','2**16')
print(r) # ['2**16']

r = re.findall('-?\d+\.?\d*','12 -36 28 1.34 -3.8')
print(r) # ['12', '-36', '28', '1.34', '-3.8']

r = re.findall('-?\d+.?\d*','12 -36 28 1.34 -3.8') # 匹配 . 需用 \ 转义,\.表示匹配 .
print(r) # ['12 ', '-36 28', '1.34', '-3.8']

r = re.findall('\$\d+','日薪:$100') # python转义\$,没有转义的东西,如果是\n就会转义成换行 --这种写法不严禁
print(r) # ['$100']

r = re.findall('\\$\\d+','日薪:$100')
print(r) # ['$100']

r = re.findall(r'\$\d+','日薪:$100')
print(r) # ['$100']

print('\\n') # \n

r = re.findall('\\\\','\\')
print(r) # ['\\']

r = re.findall(r'\\','\\') # 常使用原生字符串书写正则表达式避免多重转义的麻烦。
print(r) # ['\\']

# 贪婪模式

r = re.findall(r'ab*','abbb')
print(r)  # ['abbb'] --贪婪

r = re.findall(r'ab*?','abbb')
print(r) # ['a']--非贪婪  ,人性本贪婪,每日一问,真的需要那么多吗?--即变成不贪婪

r = re.findall(r'\(.+?\)',"(abcd)efgh(higk)")
print(r) # ['(abcd)', '(higk)']

r = re.findall(r'\(.+\)',"(abcd)efgh(higk)")
print(r)  # ['(abcd)efgh(higk)']


s = '[花千骨],[陆贞传奇],[新还珠格格],[楚乔传]'
r = re.findall(r'\[.+\]',s)
print(r) # ['[花千骨],[陆贞传奇],[新还珠格格],[楚乔传]'] 匹配到的是一个内容

r = re.findall(r'\[.+?\]',s)
print(r) # ['[花千骨]', '[陆贞传奇]', '[新还珠格格]', '[楚乔传]'] 匹配到四个


# 分组
r = re.search(r'(ab)+','ababababababab').group()
print(r) # ababababababab----加号作用与(ab)

r = re.search(r'(ab)','ababababababab').group()
print(r)  # ab ---加号作用于b

r = re.search(r'王|李\w{1,3}',"李时珍").group()
print(r) # 李时珍

r = re.search(r'王|李\w{1,3}',"王者荣耀").group() # ---王一部分,|李\w{1,3} 一部分
print(r) # 王

r = re.search(r'(王|李)\w{1,3}',"王者荣耀").group()
print(r) # 王者荣耀

r = re.search(r'(https|http|ftp|file)://\S+',"https://www.baidu.com").group(1)
print(r) # https  不加一代表获取整个字符串 https://www.baidu.com

# 捕获组

r = re.search(r'(?P<pig>ab)+',"ababababab").group() # ---给子组起个名字 称为捕获组,没名字的称为非捕获组
print(r) # ababababab

r = re.search(r'(?P<pig>ab)+',"ababababab").group('pig')
print(r) # ab

# 4. 注意事项
# 一个正则表达式中可以包含多个子组 ---一个括号就是一个子组
# 子组可以嵌套,但是不要重叠或者嵌套结构复杂
# 子组序列号一般从外到内,从左到右计数