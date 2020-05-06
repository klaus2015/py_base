# -*- coding: utf-8 -*-
import scrapy
from ..items import DnItem

class DnSpider(scrapy.Spider):
    name = 'dn'
    allowed_domains = ['www.tmooc.cn/']
    start_urls = ['http://tts.tmooc.cn/studentCenter/toMyttsPage']

    def parse(self, response):
        li_list = response.xpath('//div[@class="course-menu"]/ul/li')
        for li in li_list:
            item = DnItem()
            item['one_link'] = li.xpath('.//a/@href').get().strip()
