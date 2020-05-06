import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma
ball_type = np.dtype([
    ('position', float, 2),  # 位置(水平和垂直坐标)
    ('size', float, 1),  # 大小
    ('growth', float, 1),  # 生长速度
    ('color', float, 4)])  # 颜色(红、绿、蓝和透明度)

# 随机生成100个点对象
n = 100
balls = np.zeros(100, dtype=ball_type)
# 初始化balls数组每个字段的属性值
balls['position'] = np.random.uniform(0, 1, (n, 2))
balls['size'] = np.random.uniform(40, 70, n)
balls['growth'] = np.random.uniform(10, 20, n)
balls['color'] = np.random.uniform(0, 1, (n, 4))

mp.figure("Animation", facecolor='lightgray')
mp.title("Animation", fontsize=14)
mp.xticks([]) # 空列表表示没有刻度
mp.yticks([])

sc = mp.scatter(
    balls['position'][:, 0],
    balls['position'][:, 1],
    s=balls['size'],
    color=balls['color'], alpha=0.5)


# 定义更新函数行为
def update(number):
    balls['size'] += balls['growth']
    # 每次让一个气泡破裂，随机生成一个新的
    # 选择一个点
    boom_ind = number % n
    # 重新修改boom_ind位置元素的属性
    balls[boom_ind]['size'] = np.random.uniform(50, 70, 1)
    # balls[boom_ind]['position'] = np.random.uniform(0, 1, (1, 2))
    # 重新绘制
    sc.set_sizes(balls['size']) # 更新大小
    sc.set_offsets(balls['position']) # 更新位置


# 每隔30毫秒执行一次update更新函数，作用于mp.gcf()当前窗口对象
# mp.gcf()：	获取当前窗口
# update：		更新函数
# interval：	间隔时间（单位：毫秒）
anim = ma.FuncAnimation(mp.gcf(), update, interval=30)
mp.savefig('002.jpg')
mp.show()