# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pymongo
from .settings import *
class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        print(item['star'])
        print(item['time'])
        return item

class MaoyanMysqlPipeline:

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
        sql = 'insert into filmtab values(%s,%s,%s)'
        film_list = [
            item['name'],item['star'],item['time']
        ]
        self.cursor.execute(sql,film_list)
        self.db.commit()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
        print('我是close_spider')


class MaoyanMongoPipeline:
    def open_spider(self,spider):
        self.conn = pymongo.MongoClient(
            host=MONGO_HOST,
            port=MONGO_PORT
        )
        self.db = self.conn['mydb']
        self.myset = self.db['filmtab']
    def process_item(self,item,spider):
        film_dict = {
            'name':item['name'],
            'star':item['star'],
            'time':item['time']
        }
        self.myset.insert_one(film_dict)
        return item
    def close_spider(self,spider):
        pass




