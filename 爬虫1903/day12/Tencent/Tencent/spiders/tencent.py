# -*- coding: utf-8 -*-
import json

import scrapy
from ..items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']


    def start_requests(self):
        for pageindex in range(1,3):
            url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566816807474&countryId=&' \
                       'cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}' \
                       '&pageSize=10&language=zh-cn&area=cn'.format(pageindex)
            yield scrapy.Request(
                url=url,
                callback=self.parse_html
            )

    def parse_html(self,response):
        html = json.loads(response.text)
        item = TencentItem()
        job_list = html['Data']['Posts']
        for job in job_list:
            item['name'] = job['RecruitPostName']
            two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?' \
                      'timestamp=1568033301603&postId={}&language=zh-cn'.format(job['PostId'])
            yield scrapy.Request(
                url=two_url,
                meta={'item':item},
                callback=self.parse_two_html
            )

    def parse_two_html(self,response):
        item = response.meta['item']
        two_html = json.loads(response.text)

        item['duty'] = two_html['Data']['Responsibility']
        item['require'] = two_html['Data']['Requirement']

        yield item

