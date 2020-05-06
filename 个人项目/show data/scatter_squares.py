import matplotlib.pyplot as plt

x_values = list(range(1,1000))
y_value = [x**2 for x in x_values]
# 设置图表标题并给坐标轴加上标签
plt.scatter(x_values,y_value,c=y_value,cmap=plt.cm.Reds,edgecolors='none', s=40)
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
# plt.tick_params(axis='both', which='major',labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0,1100,0,1100000])
plt.show()
# plt.savefig('square_plot.png')