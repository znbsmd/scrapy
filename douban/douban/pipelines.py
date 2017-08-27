# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import codecs
#from scrapy.exceptions import DropItem
from douban.model.douban import Douban
from douban.model.config import DBSession
class DoubanPipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        a = Douban(pinglun=item["pinglun"].encode("utf-8"))
                    #source_site=item["source_site"].encode("utf-8"))
        self.session.add(a)
        self.session.commit()

    def close_spider(self,spider):
        self.session.close()