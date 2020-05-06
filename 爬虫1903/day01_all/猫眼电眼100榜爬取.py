"""
2、爬取猫眼电影信息 ：猫眼电影-榜单-top100榜
第1步完成：
	猫眼电影-第1页.html
	猫眼电影-第2页.html
	... ...

第2步完成：
	1、提取数据 ：电影名称、主演、上映时间
	2、先打印输出,然后再写入到本地文件
"""
"""
 1.打印程序执行时间
 2.随机的User-Agent(确保每次发请求使用随机)
 3.数据趴下来后做处理(字符串)--字典
 4.一条龙:获取--调用解析--数据处理
"""
from urllib import request
import time,re
import random
from day02_all.useragents import ua_list
import csv


class MaoyanSpider:
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset={}'

    def get_page(self,url):
        headers = {'User-Agent' : random.choice(ua_list)}
        req = request.Request(url,headers=headers)
        res = request.urlopen(req)
        html = res.read().decode('utf-8')
        self.parse_page(html)
    def parse_page(self,html):
        pattern = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?star">(.*?)</p>.*?releasetime">('
                             '.*?)</p>',re.S)
        # film_list: [('霸王别姬','张国荣','1993'),(),()]
        r_list = pattern.findall(html)

        self.write_page(r_list)


    # def write_page(self,r_list):
    #     one_film_dict = {}
    #
    #     for rt in r_list:
    #         one_film_dict['name'] = rt[0].strip()
    #         one_film_dict['star'] = rt[1].strip()
    #         one_film_dict['time'] = rt[2].strip()[5:15]
    #         print(one_film_dict)
    #  writerow 保存到csv中
    # def write_page(self,r_list):
    #     with open('mao.csv','a') as f:
    #         for rt in r_list:
    #             writer = csv.writer(f)
    #             writer.writerow([rt[0].strip(),rt[1].strip(),rt[2].strip()[5:15]])

    #  writerows 保存到csv中
    def write_page(self,r_list):
        film_lsit = []
        with open('mao1.csv','a') as f:
            writer = csv.writer(f)
            for rt in r_list:
                t = (rt[0].strip(),rt[1].strip(),rt[2].strip()[5:15])
                film_lsit.append(t)
            writer.writerows(film_lsit)

    def main(self):
        for offset in range(0, 21, 10):
            url = self.baseurl.format(offset)
            self.get_page(url)
            time.sleep(random.randint(1,3))

if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    end = time.time()
    print('执行时间:%.2f'%(end-start))