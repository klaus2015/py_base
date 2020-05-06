import numpy as np
data=[
	('zss', [90, 80, 85], 15),
	('ls', [92, 81, 83], 16),
	('ww', [95, 85, 95], 15)
]
# dtype 设置数据类型 U2 表示unicode 字符出现两次,一个unicode字符串内存占多少位 查
a = np.array(data,dtype='U2, 3int32, int32')
print(a)

# s = ['a','b','c','d']
# for i,v in enumerate(s):
#     print(i,v)

a = np.array(data,dtype=[
    ('name', 'str', 2),
    ('score', 'int32', 3),
    ('age', 'int32',1)
])
print(a)
print(a[2]['name'])

a = np.array(data,dtype={
    'names':['name', 'score', 'age'],
    'formats':['U2', '3int32', 'int32']
})
print(a)
print(a[1]['name'])
print('='*50)
f = np.array(['2011-01', '2012-01-01 10:10:50', '2013-01-01 01:01:01','2011-02-01'])
print(f,f.dtype)

f = f.astype('M8[D]') # 精确到天
print(f,f.dtype)
# 'M8[D]' ['2011-01-01' '2012-01-01' '2013-01-01' '2011-02-01'] datetime64[D]
# 'M8[s]'
# ['2011-01-01T00:00:00' '2012-01-01T10:10:50' '2013-01-01T01:01:01'
#  '2011-02-01T00:00:00'] datetime64[s]
print(f[2]-f[1]) # 366 days
