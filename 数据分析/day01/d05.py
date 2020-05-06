import numpy as np

a = np.arange(1,10)
print(a,a.shape)

# 视图变维
b = a.reshape(3,3)
print(a,'-->a')
a[0] = 999
print(b,'-->b')
"""
[[999   2   3]
 [  4   5   6]
 [  7   8   9]] -->b"""
print(b.ravel()) # 抻平数组
# [999   2   3   4   5   6   7   8   9]

# 复制变维
c = b.flatten()
print(c, '->c')
# [999   2   3   4   5   6   7   8   9] ->c
b[0][0] = 88
print(c, '->c')
# [999   2   3   4   5   6   7   8   9] ->c

# 就地变维
c.shape = (3,3)
print(c,'->c')

c.resize((9,))
print(c,'->c')
# [999   2   3   4   5   6   7   8   9] ->c