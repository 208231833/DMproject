# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from json import dumps
class ScrapygetdataPipeline(object):
    def open_spider(self,spider):
        self.filename=open("job.txt","a",encoding="utf-8")
    def process_item(self, item, spider):
        self.filename.write(dumps(dict(item),ensure_ascii=False)+'\n')
        return item
    def close_spider(self, spider):
        self.filename.close()
