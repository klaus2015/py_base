import numpy as np

a = np.arange(1,7).reshape(2,3)
b = np.arange(7,13).reshape(2,3)

print(a,'->a')
print(b,'->b')

# 水平方向
c = np.hstack((a,b))
print(c,'-->c')

a,b = np.hsplit(c,2)
print(a,'->ha')
print(b,'->hb')
print('-'*50)
# 垂直方向
c = np.vstack((a,b))
print(c,'-->c')

a,b = np.vsplit(c,2)
print(a,'->va')
print(b,'->vb')
print('-'*50)
# 深度方向  从上向下看
c = np.dstack((a,b))
print(c,'-->c')

a,b = np.dsplit(c,2)
print(a,'->da')
print(b,'->db')


# 一维数组的组合方案
a = np.arange(1,9)
b = np.arange(9,17)
print(a)
print(b)
print(np.row_stack((a, b))) # 形成两行
# [[ 1  2  3  4  5  6  7  8]
#  [ 9 10 11 12 13 14 15 16]]
print(np.column_stack((a, b))) # 形成两列
# [[ 1  9]
#  [ 2 10]
#  [ 3 11]
#  [ 4 12]
#  [ 5 13]
#  [ 6 14]
#  [ 7 15]
#  [ 8 16]]


