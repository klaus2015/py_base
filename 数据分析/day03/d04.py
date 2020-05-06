import numpy as np
import matplotlib.pyplot as mp

n = 1000
x, y = np.meshgrid(np.linspace(-3,3,n), np.linspace(-3,3,n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
print('x->',x)
print('y->',y)
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
# 上述代码可得到二位数组，x、y直接组成坐标点矩阵
# z为通过每个坐标的x与y计算而得到的高度值

# 模拟采集的海拔高度
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=20)
mp.grid(linestyle=':')
mp.contourf(x, y, z, 80, cmap='jet')
cntr = mp.contour(x,y,z,8,color='black',linewidths=0.5)
# 为等高线图添加高度标签
mp.clabel(cntr,inline_spacing=2,fmt='%.2f',fontsize=8)
mp.savefig('001.png')
mp.show()
