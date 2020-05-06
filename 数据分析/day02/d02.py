import numpy as np
import matplotlib.pyplot as mp

# 线性拆分1000个点
x = np.linspace(-np.pi, np.pi, 1000)
print(np.pi)
y = np.sin(x)
z = np.cos(x)
# 设置坐标轴范围
# mp.xlim(0,np.pi+1)
# mp.ylim(0, 1.1)

# 修改x轴的刻度文本
vals = [-np.pi,-np.pi/2,0, np.pi/2, np.pi]
texts = [r'$\pi$',r'$-\frac{\pi}{2}$','0',r'$\frac{\pi}{2}$',r'$\pi$']
mp.xticks(vals,texts)
mp.yticks([-1.0,-0.5,0.5,1.0])

# 修改坐标系
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position(('data', 0))
ax.spines['bottom'].set_position(('data', 0))

mp.plot(x, y, linestyle='--', linewidth=2,color='orangered',alpha=0.8)

mp.plot(x, z)
pointx = [np.pi/2,np.pi/2]
pointy = [1,0]
mp.scatter(pointx,pointy,marker='o',s=70,color='red',label='sample points',zorder=3)
mp.annotate(
    r'[$\frac{\pi}{2}, 1$]',			#备注中显示的文本内容
    xycoords='data',			#备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(np.pi / 2, 1),	 				#备注目标点的坐标
    textcoords='offset points',	#备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(50, 30),				#备注文本的坐标
    fontsize=14,				#备注文本的字体大小
    arrowprops=dict()			#使用字典定义文本指向目标点的箭头样式
)
"""
??????
"""
mp.show()
