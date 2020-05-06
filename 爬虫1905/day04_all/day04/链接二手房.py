import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent
class LianjiaSpider(object):
    def __init__(self):
        self.url = 'https://hz.lianjia.com/ershoufang/pg{}/'
        self.headers = {'User-Agent':'Mozilla/5.0'}
    def rand_useragent(self):
        ua = UserAgent()
        headers = {'User-Agent': ua.random}
        print(headers)
        return headers

    def get_html(self,url):
        for i in range(3):
            try:
                res = requests.get(url=url,headers=self.rand_useragent())
                res.encoding = 'utf-8'
                html = res.text

                return html
            except Exception as e:
                continue

    def parse_html(self,url):
        html = self.get_html(url)
        if html:
            parse_obj = etree.HTML(html)
            li_list = parse_obj.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
            item = {}
            print(len(li_list))
            for li in li_list:
                name_list = li.xpath('.//a[@data-el="region"]/text()')
                # 防止列表为空,直接取索引会报错,采用列表推导式
                item['name'] = [name_list[0].strip() if name_list else None][0]

                info_list = li.xpath('.//div[@class="houseInfo"]/text()')
                info_list = [info_list[0].strip().split('|') if info_list else None][0]
                if len(info_list) == 5:
                    item['model'] = info_list[1].strip()
                    item['area'] = info_list[2].strip()[:-2]
                    item['direction'] = info_list[3].strip()
                    item['perfect'] = info_list[4].strip()
                else:
                    item['model'] = item['area'] = item['direction'] = item['perfect'] = None
                item['floor'] = li.xpath('.//div[@class="positionInfo"]/text()')[0].strip().split('-')[0].strip()
                item['total_price'] = li.xpath('.//div[@class="totalPrice"]/span/text()')[0].strip()
                item['price'] = li.xpath('.//div[@class="unitPrice"]/span/text()')[0].strip()[2:-4]
                print(item)

    def main(self):
        for i in range(1,2):
            url = self.url.format(i)
            self.parse_html(url)
            time.sleep(random.uniform(0, 2))

if __name__ == '__main__':
  start = time.time()
  spider = LianjiaSpider()
  spider.main()
  spider.rand_useragent()
  end = time.time()
  print('执行时间:%.2f' % (end-start))
