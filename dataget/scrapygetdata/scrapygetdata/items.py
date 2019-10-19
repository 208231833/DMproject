# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapygetdataItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    type_id=scrapy.Field()#职业类型编号
    job_name = scrapy.Field()
    company_name=scrapy.Field()
    address=scrapy.Field()
    salary=scrapy.Field()
    education=scrapy.Field()
    time=scrapy.Field()
