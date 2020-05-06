import numpy as np
import matplotlib.pyplot as mp

apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
mp.figure('Bar', facecolor='lightgray')
mp.title('Bar Chart', fontsize=18)
mp.grid(linestyle=':')
x = np.arange(apples.size)
mp.bar(x - 0.2, apples, 0.4, color='limegreen', label='Apples001',align='center')
mp.bar(x + 0.2, oranges, 0.4, color='orangered', label='Oranges',align='center')
# 设置刻度
mp.xticks(x,['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])

mp.legend()
mp.show()