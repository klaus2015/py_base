import datetime
import random
import re
import time

import requests
from lxml import etree


class DianpingComment:
    font_size = 14
    start_y = 23

    def __init__(self, shop_id, cookies, delay=7):
        self.shop_id = shop_id
        self._delay = delay
        self.font_dict = {}
        # {'.iunsh5':'和'，'.iunsh9':'哈'}
        self._cookies = self._format_cookies(cookies)
        self._css_headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        self._default_headers = {
            'Connection': 'keep-alive',
            'Host': 'www.dianping.com',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36',
        }
        self._cur_request_url = 'http://www.dianping.com/shop/{}/review_all/p1'.format(shop_id)
        # self._cur_request_css_url = 'http://www.dianping.com/shop/{}/'.format(shop_id)

    def _delay_func(self):
        delay_time = random.randint((self._delay - 2) * 10, (self._delay + 2) * 10) * 0.1
        print('睡一会', delay_time)
        time.sleep(delay_time)

    def _format_cookies(self, cookies):
        cookies = {cookie.split('=')[0]: cookie.split('=')[1] for cookie in cookies.split('; ')}
        return cookies

    def _get_css_link(self, url):
        """
           请求评论首页，获取css样式文件
           url = http://www.dianping.com/shop/20704593/review_all
        """
        res = requests.get(url,headers=self._default_headers,cookies=self._cookies)
        html = res.text
        # print('首页源码',html)

        # css_link = re.search(r'<link re.*?css.*?href="(.*?svgtextcss.*?)">', html)
        css_link = re.findall(r'<link rel="stylesheet" type="text/css" href="//s3plus.meituan.net/v1/(.*?)">', html)
        assert css_link
        css_link = 'http://s3plus.meituan.net/v1/' + css_link[0]
        print('css链接', css_link)
        return css_link

    def _get_font_dict_by_offset(self, url):
        """
         获取坐标偏移的文字字典, 会有最少两种形式的svg文件（目前只遇到两种）
        """
        res = requests.get(url,timeout=60)
        html = res.text
        font_dict = {}
        y_list = re.findall(r'd="M0 (\d+?) ', html)
        if y_list:
            font_list = re.findall(r'textPath .*?>(.*?)<', html)
            for i, string in enumerate(font_list):
                y_offset = self.start_y - int(y_list[i])

                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font

                font_dict[y_offset] = sub_font_dict

        else:
            # [('49', '江摇够田),('49', '江摇够田)]
            font_list = re.findall(r'<text x="0" y="(.*?)">(.*?)</text>', html)

            for y, string in font_list:
                y_offset = self.start_y - int(y)
                sub_font_dict = {}
                for j, font in enumerate(string):
                    x_offset = -j * self.font_size
                    sub_font_dict[x_offset] = font
                font_dict[y_offset] = sub_font_dict
        # print('字体字典', font_dict)
        # {-26: {0: '江', -14: '摇', -28: '够'}, -76: {0: '租', -14: '贞', -28: '糠'}}
        return font_dict

    def _get_font_dict(self,url):
        """
        根据css_link 获取css样式对应文字的字典
        :param url:
        :return:
        """
        print('解析成scg成字典的css',url)
        html = requests.get(url,headers=self._css_headers,cookies=self._cookies,timeout=60).text

        # background_image_link = re.findall(r'background-image: url\((.*?)\);',html)
        background_image_link = re.findall(r'background-image: url\((.*?)\);', html)
        print('带有svg的链接', background_image_link)
        background_image_link = 'http:' + background_image_link[0]

        # pattern = re.compile(r'\.(.*?){background:(.*?).0px (.*?).0px;}',re.S)
        # group_offset_list = pattern.findall(html)
        group_offset_list = re.findall(r'\.(.*?){background:(.*?).0px (.*?).0px;}', html)
        print('css中class对应坐标', group_offset_list)
        # [('iunsh5', '-434', '-1027'), ('iunzd1', '-266', '-2159')]

        font_dict_by_offset = self._get_font_dict_by_offset(background_image_link)
        # {-26: {0: '江', -14: '摇', -28: '够'}, -76: {0: '租', -14: '贞', -28: '糠'}}
        print('解析svg成字典', font_dict_by_offset)

        for class_name, x_offset, y_offset in group_offset_list:

            # print(y_offset,x_offset)
            if font_dict_by_offset.get(int(y_offset)):
                self.font_dict[class_name] = font_dict_by_offset[int(y_offset)].get(int(x_offset))
                # print(class_name, font_dict_by_offset[int(y_offset)][int(x_offset)])
        return self.font_dict

    def _data_pipeline(self, data):
        """
        处理数据
        :param data:
        :return:
        """
        print('最终数据:', data)

    def _get_conment_page(self):  # 获得评论内容
        """
            请求评论页，并将<span></span>样式替换成文字
        """
        while self._cur_request_url:
            self._delay_func()
            print('[now_time] {msg}'.format(now_time=datetime.datetime.now(), msg=self._cur_request_url))
            res = requests.get(self._cur_request_url,headers=self._default_headers,cookies=self._cookies)
            html = res.text
            class_set = set()
            # {iungqh,iungqh,iungqh}
            for svg in re.findall(r'<svgmtsi class="(.*?)"></svgmtsi>', html):
                class_set.add(svg)
                html = re.sub(r'<svgmtsi class="%s"></svgmtsi>' % svg, self.font_dict.get(svg, ''), html)
            # for class_name in class_set:
            #     html = re.sub(r'<svgmtsi class="%s"></svgmtsi>'%class_name,self.font_dict.get(class_name,''), html)
            parse_obj = etree.HTML(html)
            self._parse_comment_page(parse_obj)
            try:
                self._default_headers['Referer'] = self._cur_request_url
                next_page_url = 'http://www.dianping.com' + parse_obj.xpath('//div[@class="reviews-pages"]//a[@class="NextPage"]'
                                                                            '/@href')[0]
            except IndexError:
                next_page_url = None
            self._cur_request_url = next_page_url

    def _parse_comment_page(self, parse_obj):
        """
        解析评论页提取数据
        :param parse_obj: parse_obj = etree.HTML(html)
        :return:
        xpath
            li_list = //div[@class="reviews-items"]/ul/li
            name = .//a[@class="name"]/text()
        """
        li_list = parse_obj.xpath('//div[@class="reviews-items"]/ul/li')
        for li in li_list:
            name = li.xpath('.//a[@class="name"]/text()')[0].strip()
            try:
                star = li.xpath('//span[@class="sml-rank-stars sml-str50 star"]/@class')[0]
                star = re.findall(r'sml-rank-stars sml-str(.*?) star', star)[0]
            except IndexError:
                star = 0
            time = li.xpath('.//span[@class="time"]/text()')[0].strip()
            pics = []
            pic_li_list = li.xpath('.//*[@class="review-pictures"]/ul/li')
            if pic_li_list:
                for pic in pic_li_list:
                    print(pic.xpath('.//a/img/@data-lazyload'))
                    pics.append(pic.xpath('.//a/img/@data-lazyload')[0])
            comment_list = li.xpath('.//div[@class="review-words Hide"]/text()|.//div[@class="review-words Hide"]/svgmtsi/@class')
            comment = ''.join(comment_list).strip()
            if not comment:
                comment_list = li.xpath(
                    './/div[@class="review-words"]/text()|.//div[@class="review-words"]/svgmtsi/@class')

            data = {
                'name': name,
                'comment': comment,
                'star': star,
                'pic': pics,
                'time': time,
            }
            self._data_pipeline(data)


    def run(self):
        self._css_link = self._get_css_link(self._cur_request_url)
        print('css 的连接', self._css_link)
        self.font_dict = self._get_font_dict(self._css_link)
        time.sleep(5)
        print('self.font_dict', self.font_dict)
        self._get_conment_page()



if __name__ == "__main__":
    COOKIES = 'cy=3; cye=hangzhou; _lxsdk_cuid=16d640e3360c8-0596a57786c2ac-5b123211-1fa400-16d640e3360c8; _lxsdk=16d640e3360c8-0596a57786c2ac-5b123211-1fa400-16d640e3360c8; _hc.v=61f6c32c-b4ca-034b-7cfb-560857f6e19e.1569341715; s_ViewType=10; _dp.ac.v=9a0a5334-6038-4d5d-8467-31d2188b8c7b; dper=4aa8ec01edab87a96bef6fa0188303f04dbb1586f50a451245c351fecdf33d66387bcdf700e51478e05e42f150895ec2f726db6badfbd185ef64ff33954838faf69a9d5e3afe13a7c526b93c211055405b0b88a11f413b1463f48f0fe712940f; ua=dpuser_5306889493; ctu=87ef40fb04698d95ad55db24756553d956249ee29549931fd78a8a00470a6385; ll=7fd06e815b796be3df069dec7836c3df; _lxsdk_s=16dc5efce18-998-020-b33%7C%7C1'
    dp = DianpingComment('67161528', cookies=COOKIES)
    dp.run()
