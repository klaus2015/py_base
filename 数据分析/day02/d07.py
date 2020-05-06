# 刻度定位器
import matplotlib.pyplot as mp

mp.figure('locators',facecolor='lightgray')
mp.xlim(1,10)
ax = mp.gca()
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
ax.spines['left'].set_color('none')
ax.spines['bottom'].set_position(('data', 0.5))
ax.xaxis.set_major_locator(mp.MultipleLocator(1))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
mp.show()