import matplotlib.pyplot as plt
from random_walk import RandomWalk

while True:
    # 创建一个RandomWalk实例,并将其包含的点都绘制出来
    rw = RandomWalk(50000)
    rw.fill_walk()
    # 设置绘图窗口的尺寸
    plt.figure(dpi=300,figsize=(16,9))
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values,c=point_numbers,cmap=plt.cm.Blues,edgecolors='none', s=1)
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    # plt.show()
    plt.savefig('square_plot003.png')

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break
