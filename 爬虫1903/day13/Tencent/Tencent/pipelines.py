# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class TencentPipeline(object):
    def process_item(self, item, spider):
        print(dict(item))
        return item

class TencentMysqlPipeline:
    def open_spider(self,spider):
        self.db = pymysql.connect(
            '176.23.4.36','tiger','123456','maoyan',charset='utf8'
        )
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins  = 'insert into job1 values(%s,%s,%s,%s)'
        job_list = [item['zh_name'],item['zh_type'],item['zh_duty'],item['zh_require']]
        self.cursor.execute(ins,job_list)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()

