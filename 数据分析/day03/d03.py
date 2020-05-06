import numpy as np
import matplotlib.pyplot as mp
mp.figure('pie', facecolor='lightgray')
#整理数据
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']
mp.figure('Pip Chart')
mp.title('Pip', fontsize=20)
mp.axis('equal') # 设置x与y轴等比例输出
mp.pie(values,spaces,labels,colors,'%.1f%%',shadow=True)
mp.legend()
mp.show()