# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem
import os
class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url = 'https://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'
    dir = '/home/tarena/images/'
    if not os.path.exists(dir):
        os.makedirs(dir)
    def start_requests(self):
        for pn in range(0,100,30):
            url = self.url.format(pn)
            yield scrapy.Request(
                url=url,
                callback=self.parse_image
            )

    def parse_image(self,response):
        item = SoItem()
        html = json.loads(response.text)
        for img in html['list']:
            item['img_link'] = img['qhimg_url']
            item['img_title'] = img['title']
            yield item

    def parse(self, response):
        pass
