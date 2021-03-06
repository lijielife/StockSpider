# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import NovelspiderItem  #这里的Novelspider其实是没有用到的，可以删除
from scrapy.conf import settings
import pymongo

class NovelspiderPipeline(object):

    def process_item(self, item, spider):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        client = pymongo.MongoClient(host=host, port=port)
        dbName = item['stockCode']
        tdb = client[dbName]

        if spider.name == 'novspider':
            self.post = tdb['GuYouHui']
        elif(spider.name == 'newsspider'):
            self.post = tdb['XinWen']
        elif(spider.name == 'researchspider'):
            self.post = tdb['YanBao']
        elif(spider.name == 'publicspider'):
            self.post = tdb['GongGao']

        bookInfo = dict(item)
        self.post.insert(bookInfo)
        return item
