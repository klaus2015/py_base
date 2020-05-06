"""
select函数
"""

from select import select
from socket import *

s = socket()
s.bind(('0.0.0.0',20191))
s.listen(3)

f = open('a','rb')

print("监控IO")
rs,ws,xs = select([s],[f],[]) # 返回值是列表
print('rlist:',rs)  #  rlist: []
print('wlist:',ws)  #  wlist: [<_io.BufferedReader name='a'>]
print('xlist:',xs)  #   xlist: []