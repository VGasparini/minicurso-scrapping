#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class NoticiasPipeline(object):

    def open_spider(self, spider):
      self.file = open('notices.json', 'w')

    def close_spider(self, spider):
      self.file.close()

    def process_item(self, item, spider):
      line =  json.dumps(dict(item), ensure_ascii=False).encode('utf8') + '\n'
      self.file.write(line)
      return item
