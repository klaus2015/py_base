import requests

import random
import requests

from useragents import *

# 获取随机headers
def get_headers():
    headers = {'User-Agent':random.choice(ua_list)}

    return headers

def total_number():
    # F12抓包抓到的地址
    url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(17)
    headers = get_headers()
    html = requests.get(url=url, headers=headers).json()
    total = int(html['total'])
    print(html)
    print(total)

total_number()


