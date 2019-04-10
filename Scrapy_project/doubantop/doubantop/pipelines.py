# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo


class DoubantopPipeline(object):
    collection_name = 'scrapy_items'  # 这里的地方是连接的数据库表的名字
 
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db
 
    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),  # get中有两个参数，一个是 配置的MONGO_URL ，另一个是localhost
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'scrapy_items')  # 这里的两个参数,第一个是数据库配置的.第二个是它的表的数据库的名字
            )
    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]
 
    def close_spider(self, spider):
        self.client.close()
 
    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item
