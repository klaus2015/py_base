# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from .settings import *
import pymongo
class TencentPipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        print(item['duty'])
        print(item['require'])


        return item

class TencentMysqlPipeline:

    def open_spider(self,spider):
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=MYSQL_CHAR
        )
        self.cursor = self.db.cursor()
        print('我是open_spider')

    def process_item(self, item, spider):
        sql = 'insert into job values(%s,%s,%s)'
        job_info = [item['name'],item['duty'],item['require']]
        self.cursor.execute(sql,job_info)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print("我是close_spider函数")

class TencentMongoPipeline:
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(
            host=MONGO_HOST,
            port=MONGO_PORT
        )
        self.db = self.conn['tx']
        self.myset = self.db['job']

    def process_item(self,item,spider):
        job_dict = {
            'name':item['name'],
            'duty':item['duty'],
            'require':item['require']
        }
        self.myset.insert_one(job_dict)
        return item

    def close_spider(self, spider):
        pass