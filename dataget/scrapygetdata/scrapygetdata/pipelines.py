# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
class ScrapygetdataPipeline(object):
    def open_spider(self,spider):
        self.conn = pymysql.connect(host='127.0.0.1', user='root', password='root', database='dmproject', port=3306)
        self.cur=self.conn.cursor()
    def process_item(self, item, spider):
        sql = r"""
        insert into job values (DEFAULT,'{}','{}','{}','{}','{}','{}','{}')
        """.format(item['type_id'],item['job_name'],item['company_name'],item['address'],item['salary'],item['education'],item['time'].replace(' ','-').replace(':','-'))
        print(sql)
        try:
            self.cur.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
            print("插入失败")
        return item
    def close_spider(self, spider):
        self.conn.close()
