# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from .settings import *
class MaoyanPipeline(object):
    def process_item(self, item, spider):
        print(item['name'])
        print(item['star'])
        print(item['time'])

        return item

# 第一一个mysql管道类
class MaoyanMysqlPipeline:

    def open_spider(self, spider):
        # 爬虫程序启动时,只执行一次,一般用于建立数据库连接
        self.db = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PWD,
            database=MYSQL_DB,
            charset=MYSQL_CHAR
        )
        self.cursor = self.db.cursor()
        print('woshi open_spider')

    def process_item(self, item, spider):
        ins = 'insert into filmtab values(%s,%s,%s)'
        file_list = [
            item['name'],item['star'],item['time']
        ]
        self.cursor.execute(ins,file_list)
        self.db.commit()
        return item

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()
        print("我是close_spider函数")

import pymongo

class MaoyanMongoPipeline:
    def open_spider(self,spider):
        # 连接对象
        self.conn = pymongo.MongoClient(
            host=MONGO_HOST,
            port=MONGO_PORT
        )
        # 库对象
        self.db = self.conn['mydb']
        # 集合(表)对象
        self.myset = self.db['filmtab']

    def process_item(self,item,spider):
        film_dict = {
            '电影名称':item['name'],
            '电影主演':item['star'],
            '上映时间':item['time']
        }
        self.myset.insert_one(film_dict)
        return item

    def close_spider(self, spider):
        pass