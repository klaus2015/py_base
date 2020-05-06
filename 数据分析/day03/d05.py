import numpy as np
import matplotlib.pyplot as mp

n = 100
x, y = np.meshgrid(np.linspace(-3,3,n), np.linspace(-3,3,n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
print('x->',x)
print('y->',y)
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)

mp.imshow(z,cmap='jet',origin='lower')
mp.colorbar()
mp.show()