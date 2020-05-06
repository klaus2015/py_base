# -*- coding: utf-8 -*-
import scrapy
from ..items import DaomuItem

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']

    # 解析一级页面
    def parse(self, response):
        link_list = response.xpath('//ul[@class="sub-menu"]/li/a/@href').extract()
        print(link_list)
        for link in link_list:
            yield scrapy.Request(
                url=link,
                callback=self.parse_two_html
            )
    def parse_two_html(self,response):
        article_list = response.xpath('//article')
        for article in article_list:
            item = DaomuItem()
            info_list = article.xpath('./a/text()').get().split()
            item['volume_name'] = info_list[0]
            item['zh_num'] = info_list[1]
            item['zh_name'] = info_list[2]
            # 提取链接,并发送给调度器入队列
            item['zh_link'] = article.xpath('./a/@href').get()
            yield scrapy.Request(
                url=item['zh_link'],
                meta={'item':item},
                callback=self.parse_three_html
            )

    def parse_three_html(self,response):
        item = response.meta['item']
        content_list = response.xpath('//article[@class="article-content"]//p/text()').extract()
        item['zh_content'] = '\n'.join(content_list)
        yield item