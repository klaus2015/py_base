
from urllib import request
import time,re
import random
from day02_all.useragents import ua_list
import pymysql


class MaoyanSpider:
    def __init__(self):
        self.baseurl = 'https://maoyan.com/board/4?offset={}'
        self.db = pymysql.connect('localhost','root','123456','maoyan',
            charset='utf8')
        self.cursor = self.db.cursor()

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
        film_list = pattern.findall(html)

        self.write_page(film_list)

    #  writerows 保存到csv中
    def write_page(self,film_list):
        sql = 'insert into filmtab values(%s,%s,%s)'
        data_list = []
        for film in film_list:
            L = [
                film[0].strip(),
                film[1].strip(),
                film[2].strip()[5:15]
            ]
            data_list.append(L)
        self.cursor.executemany(sql,data_list)
        self.db.commit()



    def main(self):
        for offset in range(0, 91, 10):
            url = self.baseurl.format(offset)
            self.get_page(url)
            time.sleep(random.randint(1,3))

if __name__ == '__main__':
    start = time.time()
    spider = MaoyanSpider()
    spider.main()
    end = time.time()
    print('执行时间:%.2f'%(end-start))