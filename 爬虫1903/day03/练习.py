
import requests
from lxml import etree
import time
import random
""""""

class BaiduImageSpider:
    def __init__(self):
        self.ua_list = [
            'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0',
            'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'
        ]
        self.headers = {"User-Agent": random.choice(self.ua_list)}

    # 获取帖子链接
    def get_tlink(self,url):
        parse_html = self.get_parse_html(url)
        t_list = parse_html.xpath('//*[@id="thread_list"]/li//div[@class="t_con cleafix"]/div/div/div/a/@href')
        # print(len(t_list))
        for t in t_list:
            t_link = 'http://tieba.baidu.com' + t
            self.write_image(t_link)
        print(t_list)

    def get_parse_html(self, url):

        html = requests.get(url, headers=self.headers).content.decode('utf-8')
        # 提取帖子链接
        parse_html = etree.HTML(html)
        return parse_html

    def write_image(self,t_link):
        parse_html = self.get_parse_html(t_link)
        img_list = parse_html.xpath('//img[@class="BDE_Image"]/@src | //div['
                                    '@class="video_src_wrapper"]/embed/@data-video')
        for img_link in img_list:
            html = requests.get(img_link,headers=self.headers).content
            filename = img_link[-10:]
            with open(filename,'wb') as f:
                f.write(html)
                print('%s下载成功' % filename)
                time.sleep(random.randint(1,3))







if __name__ == "__main__":
    spider = BaiduImageSpider()
    spider.get_tlink('http://tieba.baidu.com/f?kw=%E6%9F%B3%E5%B2%A9&ie=utf-8&pn=0')



