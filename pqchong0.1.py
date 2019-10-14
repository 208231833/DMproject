#coding=utf-8
"""
开始尝试爬取
爬到文件里面
第一个版本是静态的获取HTML
"""
from urllib.request import Request
from urllib.request import urlopen
from random import choice
import ssl
def gethtml(url):
    print(url)
    ca=ssl._create_unverified_context()
    user_agents = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:69.0) Gecko/20100101 Firefox/69.0',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.42 Safari/537.36'
    ]
    headers = {"User-Agent": choice(user_agents)}
    req=Request(url,headers=headers)
    resp=urlopen(req,context=ca)
    return resp.read().decode()
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
        if  i==189:
            break

if __name__=="__main__":
    main()