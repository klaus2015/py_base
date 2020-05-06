import numpy as np
a = np.arange(1, 11)
mask = [True, False,True, False,True, False,True, False,True, False]
print(a[mask])

b = np.arange(1,100)
print(b[b % 3 ==0])
# [ 3  6  9 12 15 18 21 24 27 30 33 36 39 42 45 48 51 54 57 60 63 66 69 72
#  75 78 81 84 87 90 93 96 99]

mask = (b%3 == 0) & (b % 7 == 0)
print(mask)
print(b[mask]) # [21 42 63 84]
print('-'*50)

# 基于索引的排名
names = np.array(['Apple','Mate30 pro','MI','oppo','vivo'])
rank = [1,0,3,4,2]
print(names[rank])
# ['Mate30 pro' 'Apple' 'oppo' 'vivo' 'MI']