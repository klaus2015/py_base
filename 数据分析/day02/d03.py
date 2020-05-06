import matplotlib.pyplot as mp

mp.figure('A Figure', facecolor='lightgray')
mp.plot([0,1],[0,2])

mp.title('A Figure', fontsize=18)
mp.xlabel('time', fontsize=14)
mp.ylabel('price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
"""
??????
"""

mp.figure('B Figure', facecolor='gray')
mp.plot([0,1],[0,2])

mp.show()