import numpy as np

c = np.arange(1,19)

# 页， 行， 列
c.shape = (3, 2, 3) # 3页，两行，三列
print(c)
print(c[0][1][0])
print(c.shape)