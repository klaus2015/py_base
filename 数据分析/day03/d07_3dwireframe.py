import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d
n = 1000
x, y = np.meshgrid(np.linspace(-3,3,n), np.linspace(-3,3,n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
print('x->',x)
print('y->',y)
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
# 上述代码可得到二位数组，x、y直接组成坐标点矩阵
# z为通过每个坐标的x与y计算而得到的高度值

# 模拟采集的海拔高度
mp.figure('3D Surface', facecolor='lightgray')
ax3d = mp.gca(projection='3d')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
ax3d.plot_wireframe(x,y,z,rstride=30,cstride=30,
	linewidth=1, color='dodgerblue')

mp.show()