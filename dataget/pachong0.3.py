#coding=utf-8
#coding=utf-8
"""
用x-path来提取数据
展示到控制台
"""
import requests
from fake_useragent import UserAgent
from lxml import etree
from time import sleep
import ssl
def gethtml(url):
    """
    页面爬取
    :param url:
    :return:
    """
    headers = {"User-Agent":UserAgent().random}
    resp=requests.get(url,headers=headers)
    resp.encoding="utf-8"
    return resp.text
def savedata(html):
    """
    把html中的每一行数据获取下来
    并且以一个列表的形式返回回爬取结果
    :param html:
    :return doc:
    """
    e=etree.HTML(html)
    job=data_format(e.xpath('//tr[@class="bg"]/td[2]/a/text()'))
    company_name= data_format(e.xpath('//tr[@class="bg"]/td[3]/a/text()'))
    address = data_format(e.xpath('//tr[@class="bg"]/td[4]/a/text()'))
    salary= data_format(e.xpath('//tr[@class="bg"]/td[5]/a/text()'))
    education=data_format(e.xpath('//tr[@class="bg"]/td[6]/a/text()'))
    publish_time=data_format(e.xpath('//tr[@class="bg"]/td[7]/a/text()'))
    print(len(job),len(company_name),len(address),len(salary),len(education),len(publish_time))
    info=[]
    for i in range(len(job)):
        temp={"job":job[i],"compan_name":company_name[i],"address":address[i],"salary":salary[i],"education":education[i],"publish_time":publish_time[i]}
        info.append(temp)
    return info
def data_format(data):
    list=[]
    for i in data:
        i=i.encode("utf-8").decode("utf-8")
        i=i.strip()
        list.append(i)
    return list
def main():
    num=int(input("请输入您要爬取多少页:"))
    allinfo=[]
    for i in range(num):
        url = "http://www.xmrc.com.cn/net/info/resultg.aspx?a=a&g=g&jobtype=9902&releaseTime=365&searchtype=1&keyword=&sortby=updatetime&ascdesc=Desc&PageIndex ={}".format(i)
        info=gethtml(url)
        info=savedata(info)
        allinfo.extend(info)
        sleep(3)#睡眠三秒防止被GANK
    print(len(allinfo))
if __name__=="__main__":
    main()