# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import SoItem
class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    def start_requests(self):
        url = 'https://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'
        for i in range(15):
            sn = i * 30
            full_url = url.format(sn)
            yield scrapy.Request(
                url=full_url,
                callback=self.parse_image
            )
    def parse_image(self,response):
        html = json.loads(response.text)
        item = SoItem()
        for img in html['list']:

            item['img_link'] = img['qhimg_url']
            item['img_title'] = img['title']
            yield item


    def parse(self, response):
        pass
#https://image.so.com/zjl?ch=beauty&sn=0&listtype=new&temp=1