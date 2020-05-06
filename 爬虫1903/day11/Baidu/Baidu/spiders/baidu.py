# -*- coding: utf-8 -*-
import scrapy


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        # title = response.xpath('/html/head/title/text()')
        # title=[<Selector xpath='/html/head/title/text()' data='百度一下，你就知道'>]
        # print(title.get('title')) --百度一下，你就知道
        title = response.xpath('/html/head/title/text()').get()
        print('*'*50)
        print('*' * 50)
        print(title) # ['百度一下，你就知道']
        print('*' * 50)
