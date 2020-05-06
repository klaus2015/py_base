import requests
from lxml import etree
import pymysql
import re
class Goverment:
    def __init__(self):
        self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
        self.headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
        }
        self.db = pymysql.connect(
            'localhost','root','123456','govdb',charset='utf8'
        )
        self.cursor = self.db.cursor()


    def get_false_link(self):
        html = requests.get(url=self.one_url,headers=self.headers).text

        parse_html = etree.HTML(html)
        res = parse_html.xpath('//a[@class="artitlelist"]')
        for a in res:
            if re.findall('.*?以上行政区划代码',a.get('title'),re.S):
                two_false_link = 'http://www.mca.gov.cn' +a.get('href')
                return two_false_link
    def get_true_link(self,two_false_link ):
        html = requests.get(url=two_false_link,headers=self.headers).text
        pattern = re.compile('window.location.href="(.*?)"')
        real_link = pattern.findall(html,re.S)[0]
        print(real_link)

        sql = 'select * from version where link="{}"'.format(real_link)
        self.cursor.execute(sql)
        if self.cursor.fetchall():
            print("数据是最新的,不需要抓取数据")
        else:
            self.get_data(real_link)
            ins = 'insert into version values (%s)'
            self.cursor.execute(ins,[real_link])
            self.db.commit()
    # 提取数据
    def get_data(self, real_link):
        html = requests.get(url=real_link, headers=self.headers).content.decode('utf-8', 'ignore')
        # //tr[@height="19"]          code: td[2]/text()   city:  td[3]/text()
        parse = etree.HTML(html)
        tr_list = parse.xpath('//tr[@height="19"]')
        for tr in tr_list:
            code = tr.xpath('./td[2]/text()')[0]
            name = tr.xpath('./td[3]/text()')[0]
            print(code,name)
    def main(self):
        two_false_link = self.get_false_link()
        self.get_true_link(two_false_link)



if __name__ == "__main__":
    spider = Goverment()
    spider.main()


