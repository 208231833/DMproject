# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import ScrapygetdataItem

class XmrcSpider(scrapy.Spider):
    name = 'xmrc'
    allowed_domains = ['xmrc.com.cn']
    start_urls = []
    for i in range(1,7):
        #基础url
        basis_url="http://www.xmrc.com.cn/net/info/resultg.aspx?a=a&g=g&jobtype=990{}&releaseTime=365&searchtype=1&keyword=&sortby=updatetime&ascdesc=Desc&PageIndex=1"
        start_urls.append(basis_url.format(i))
    def parse(self, response):
        job_names = response.xpath('//tr[@class="bg"]/td[2]/a/text()').extract()
        company_names = response.xpath('//tr[@class="bg"]/td[3]/a/text()').extract()
        addresss = response.xpath('//tr[@class="bg"]/td[4]/a/text()').extract()
        salarys = response.xpath('//tr[@class="bg"]/td[5]/a/text()').extract()
        educations = response.xpath('//tr[@class="bg"]/td[6]/a/text()').extract()
        times = response.xpath('//tr[@class="bg"]/td[7]/a/text()').extract()
        item =ScrapygetdataItem()
        type_id=re.search("jobtype=(\w*)",response.url).group(1)
        pageindex=re.search("PageIndex=(\w*)",response.url).group(1)
        for job_name,company_name,address,salary,education,time in zip(job_names,company_names,addresss,salarys,educations,times):
            item['type_id']=type_id
            item['job_name']=job_name.strip()
            item['company_name']=company_name.strip()
            item['address']=address.strip()
            item['salary']=salary.strip()
            item['education']=education.strip()
            item['time']=time.strip()
            yield item
        next_url=response.xpath('//a[@disabled="true"]/text()').extract_first()
        if next_url != "下页":
            yield scrapy.Request("http://www.xmrc.com.cn/net/info/resultg.aspx?a=a&g=g&jobtype={}&releaseTime=365&searchtype=1&keyword=&sortby=updatetime&ascdesc=Desc&PageIndex={}".format(type_id,int(pageindex)+1),callback=self.parse)
