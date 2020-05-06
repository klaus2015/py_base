# -*- coding: utf-8 -*-
import scrapy
import json
from ..items import TencentItem
# 使用redis_key改写,导入scrapy_redis的RedisSpider
from scrapy_redis.spiders import RedisSpider

# 继承RedisSpider类
class TencentSpider(RedisSpider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'
    # 1. 去掉start_urls
    # 项目启动时,阻塞,等待redis发送的指令(URL)
    redis_key = 'tencent:spider'

    def parse(self, response):
        for page_index in range(1,51):
            url = self.one_url.format(page_index)
            yield scrapy.Request(
                url = url,
                callback = self.parse_one
            )

    def parse_one(self,response):
        html = json.loads(response.text)
        for job in html['Data']['Posts']:
            item = TencentItem()
            # 职位名称
            item['zh_name'] = job['RecruitPostName']
            item['zh_type'] = job['CategoryName']
            # postId: 拼接二级页面的地址
            post_id = job['PostId']
            two_url = self.two_url.format(post_id)
            # 交给调度器
            yield scrapy.Request(
                url = two_url,
                meta = {'item':item},
                callback = self.parse_two
            )

    def parse_two(self,response):
        item = response.meta['item']
        html = json.loads(response.text)
        # 职责
        item['zh_duty'] = html['Data']['Responsibility']
        # 要求
        item['zh_require'] = html['Data']['Requirement']

        yield item
















