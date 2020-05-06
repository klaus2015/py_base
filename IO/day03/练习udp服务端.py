"""
广播发送
1. 创建udp套接字
2. 设置套接字可以发送接收广播　（setsockopt）
3. 选择接收的端口
4. 接收广播
"""
from socket import *
from time import sleep

s = socket(AF_INET,SOCK_DGRAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
ADDR = ('176.23.4.255',8000)

data = """******************
            杭州 天气预报
            温度:27.9℃
            小雨
            星期六
"""
while True:
    sleep(2)
    s.sendto(data.encode(),ADDR)

