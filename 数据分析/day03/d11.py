import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md
# 日期转换函数
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	t = time.strftime('%Y-%m-%d')
	return t
# 直接读取该文件并且获取ndarray数组对象
# 返回值：
#     unpack=False：返回一个二维数组
#     unpack=True： 多个一维数组
dates,opening_prices,highest_prices,low_prices,close_price = np.loadtxt(
    '../da_data/aapl.csv',			# 文件路径
    delimiter=',',			# 分隔符
    usecols=(1, 3,4,5,6),			# 读取1、3两列 （下标从0开始）
    unpack=True,			# 是否按列拆包
    converters={1: dmy2ymd},
    dtype='M8[D], f8,f8,f8,f8',		# 制定返回每一列数组中元素的类型
    		# 转换器函数字典
)

# 绘制收盘价格的折线图
mp.figure('AAPL',facecolor='lightgray')
mp.title('AAPL',fontsize=16)
mp.xlabel('Date',fontsize=14)
mp.ylabel('closing price',fontsize=14)
#拿到坐标轴
ax = mp.gca()
#设置主刻度定位器为周定位器（每周一显示主刻度文本）
ax.xaxis.set_major_locator( md.WeekdayLocator(byweekday=md.MO) )
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates,close_price,color='dodgerblue',label='AAPL',linestyle='--',linewidth=2)
mp.legend()
# 自动格式化x轴的日期
mp.gcf().autofmt_xdate()
mp.gcf().autofmt_ydate()
mp.show()

