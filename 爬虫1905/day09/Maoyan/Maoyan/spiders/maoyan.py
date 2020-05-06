# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maaoyan.com']
    start_urls = ['https://maoyan.com/board/4']

    def parse(self, response):
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        item = MaoyanItem()
        for dd in dd_list:
            item['name'] = dd.xpath('./a/@title').extract_first().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract_first().strip()
            yield item

