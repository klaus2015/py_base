import matplotlib.pyplot as mp

mp.figure('Subplot',facecolor='lightgray')

for i in range(1,37):
    mp.subplot(6,6,i)
    # mp.subplot(331) 也可以
    mp.text(0.5, 0.5, i, ha='center',
            va='center', size=36,alpha=0.6)
    mp.xticks([])
    mp.yticks([])
    mp.tight_layout()
mp.show()