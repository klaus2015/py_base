# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入scrapy的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy

# 1. 继承 ImagesPipeline
# 2. 重写 类内方法
class SoPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        # 把图片链接发给调度器
        yield scrapy.Request(url = item['img_link'],dont_filter=False)











