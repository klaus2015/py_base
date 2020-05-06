# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4?offset=0']
    offset = 0

    def parse(self, response):
        # 基准xpath
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        for dd in dd_list:
            item = MaoyanItem()

            # 电影名称
            item['name'] = dd.xpath('./a/@title').extract_first().strip()
            # 电影主演
            item['star'] = dd.xpath('.//p[@class="star"]/text()').extract_first().strip()

            # 上映时间
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').extract_first().strip()

            # 把爬去的数据交给文件pipeline处理
            yield item
        self.offset += 10
        if self.offset <= 90:
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
            yield scrapy.Request(
                url=url,
                callback=self.parse
            )