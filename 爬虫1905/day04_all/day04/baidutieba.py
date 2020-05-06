import requests
from lxml import etree
import time
import random
import time
from urllib import parse

class BaiduImageSpider:
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?kw={}&ie=utf-8&pn={}'
        self.headers = {'User-Agent':'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)'}

    def get_html(self,url):
        res = requests.get(url=url,headers=self.headers)
        html = res.content
        return html

    def xpath_fun(self,html,xpath_bds):
        parse_obj = etree.HTML(html)
        r_list = parse_obj.xpath(xpath_bds)
        return r_list

    def parse_html(self,url):
        one_html = self.get_html(url).decode()
        xpath_bds = '//li[@class=" j_thread_list clearfix"]//a[@class="j_th_tit "]/@href'
        t_list = self.xpath_fun(one_html,xpath_bds)
        for tlink in t_list:
            tlink = 'http://tieba.baidu.com' + tlink
            # 对帖子链接发请求,获取图片链接,向图片链接发求情,保存图片
            self.get_image(tlink)

    def get_image(self,tlink):
        html = self.get_html(tlink).decode()
        xpath_bds = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src'
        img_link_list = self.xpath_fun(html,xpath_bds)
        for img_link in img_link_list:
            self.save_image(img_link)

    def save_image(self,img_link):
        html = self.get_html(img_link)
        filename = img_link[-10:]
        with open(filename,'wb') as f:
            f.write(html)
        print('下载成功')

    def main(self):
        name = input('请输入贴吧名: ')
        star = int(input('起始页:'))
        end = int(input('终止页:'))

        for page in range(star,end+1):
            pn = (page - 1) * 50
            name = parse.quote(name)
            url = self.url.format(name,page)
            self.parse_html(url)
            time.sleep(random.randint(1,3))

if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.main()