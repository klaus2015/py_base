import numpy as np
import matplotlib.pyplot as mp

x = np.array([1,2,3,4,5,6])
y = np.array([20,37,40,4,60,10])

mp.hlines([10,30,20],1,6)
mp.vlines(4,10,35)


mp.plot(x, y)
mp.show()
