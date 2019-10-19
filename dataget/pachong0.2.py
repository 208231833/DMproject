#coding=utf-8
#coding=utf-8
"""
改进版本运用
request库来爬取
"""
import requests
from fake_useragent import UserAgent
import ssl
def gethtml(url):
    headers = {"User-Agent":UserAgent().random}
    resp=requests.get(url,headers=headers)
    resp.encoding="utf-8"
    return resp.text
def savehtml(html):
    with open("data","a",encoding="utf-8") as f:
        f.write(html)
def main():
    url="http://www.xmrc.com.cn/net/info/resultg.aspx?a=a&g=g&jobtype=9902&releaseTime=365&searchtype=1&keyword=&sortby=updatetime&ascdesc=Desc&PageIndex ={}"
    i = 1
    while(True):
        info=gethtml(url.format(i))
        savehtml(info)
        i+=1
        print(i)
        if  i==189:
            break
if __name__=="__main__":
    main()