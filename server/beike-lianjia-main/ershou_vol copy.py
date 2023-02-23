#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import requests as req
import json
import re
from fake_useragent import UserAgent
from lib.spider.base_spider import BaseSpider

# 此平台需要登录
# s = req.Session()
headers = {
    "Cookie": "SECKEY_ABVK=nQYk1Jpn7q8U08iDBjTdqdN2ooAFIwaAw1Qd/FxFBjs%3D; BMAP_SECKEY=nkvAt5QlUwhHgkkgqKOqOkO2Wyx3HYsDSmQJ5Tgy1Uvjtd3sVCHpK8_blH-L2L00qPZfb0tyDUIOTn43-lZ48BPRxgmn1mE00dEAyp-BWJwAaRn0Oiccm3JwEX9bGWvz894k9YtSr1GIqoxSz2EZrwmJdRAQUh7NRRn8U_uZJ0nfxEPfPQJ8fjrnsqZkJM2P; lianjia_uuid=ad89a543-48c8-4d36-876d-28d3abc7878c; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1676966895; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218673042936d5a-01491bd4cebb17-1f525634-1296000-18673042937dbe%22%2C%22%24device_id%22%3A%2218673042936d5a-01491bd4cebb17-1f525634-1296000-18673042937dbe%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; beikeBaseData=%7B%22parentSceneId%22%3A%22%22%7D; crosSdkDT2019DeviceId=-7y9013--scnacd-b219ffsqhyml5de-o4olx0x7w; select_city=330100; lianjia_ssid=477099f4-5f6e-4d40-af51-9ea5e0e4f6a3; login_ucid=2000000025257194; lianjia_token=2.00139f201d6b87291b0232092c1fd93035; lianjia_token_secure=2.00139f201d6b87291b0232092c1fd93035; security_ticket=LJOx8wE5uO9C6nu3KJzT7QxCHZccjBObnLvRxzARsD9zrfWAuMHlMu8w31q6nVlvfl8ZGklSz1LmQUV/D+OH3ufrx6FnfnBS25iOzsZyvcW8EniU5KtSSx5oxUnShLzhiTggGtdFFJdGvkNjm3yvoLNytYt4TlWtlj+ITSnw64U=; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1677072236; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYjhjMTg1YmFmZjJkNGMwNTYwNmFiYzY3MDg3NGE1NjgzODI0MWY1M2JmZGU0YzJmNjBjOTE5YzRiMTM5M2Q5M2Q2MWQzOTI0MWE2MGJhYmVmNTI2MGI1ODc1NTgxNWNiYzFlY2Y5MTNiOWQyYmIwYTUxOTVhNmE3Mzg4YmI3NjMyZjQzMmNlYjliYTBmNWNiZmJjZjBiMzZlMWM1YjU1ZmZkOWY5N2IyYThjOTFiNDdkYmYxMDg2Yjc1MzNmZTQ2OTk4ZDZmMjEyM2FmZWU3Mjk4ZTI1YWMyMDQzNzNhMTBmYmI1NWNkYzMwYmMxZTJhM2FmMzU1MTE2ODkyMjM0OVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI5MDk1NDExOVwifSIsInIiOiJodHRwczovL2h6LmtlLmNvbS9jaGVuZ2ppYW8veGlodS9wZzEvIiwib3MiOiJ3ZWIiLCJ2IjoiMC4xIn0=; cy_ip=125.119.189.250; f-token=WG8v47jTJnvEG0ndfBCtVrUQ0jayjjguO5LKh/i36gCdK9E6wlIhGC2cd9GE16veo0Nj2m+XVYgx89tLkcDQTvp4uZzicsLMeILC09zwXqDoHn5//bQtzgZmYKhcHRNDS80JzoD1ZAsrgHqT/Os=",
    'User-Agent': UserAgent().random,  # 使用第三方库生成的随机UA
    # "Accept-Encoding": "gzip, deflate, br"
    'Referer': 'https://clogin.ke.com/'
}

def download(url,start,end):
    for i in range(end):
        getListInfo(url,str(i+1))
# print(requests.text)
# <a  class="" href="https://hf.ke.com/ershoufang/" >二手房
# (\ < a href=\")(https:\/\/bj\.lianjia\.com\/chengjiao/[0-9]+\.html)
# h += 1
# getListInfo(httpLink + "/chengjiao/pg" + str(i + 1) + "/", h, file)
def getListInfo():
    fp = open('hoseLink.txt', 'r')
    httpLink = "-1"
    h = 0
    k = 0
    while httpLink != '':
        httpLink = fp.readline()
        if httpLink == '':
            break
        httpLink = httpLink.strip('\n')
        url = httpLink + "/chengjiao/pg1/"
        BaseSpider.random_delay()
        requests = req.get(url,timeout=10,headers=headers)
        print(url)
        # print(headers)
        print(requests.text)
        patternname = re.compile("city_name: '[\u4E00-\u9FA5]+")
        nameList = patternname.findall(requests.text)
        name = nameList[0].replace("city_name: '", "")
        file = open(str(name)+".txt",'a+')
        k += 1
        for i in range(1):
            h+=1
            BaseSpider.random_delay()
            requests = req.get(httpLink + "/chengjiao/pg" + str(i + 1) + "/",timeout=10,headers=headers)
            pattern = re.compile("(\<a href=\")("+httpLink+"\/chengjiao\/[a-zA-Z0-9]+\.html)")
            resultList = pattern.findall(requests.text)
            resultList = list(map(lambda x:x[1],resultList))
            for i in range(len(resultList)):
                file.write(str(resultList[i]) + '\n')
            print("完成数据收集第" + str(h) + "条")
        print("-------------------完成数据收集第" + str(k) + "条")
        h=0
        file.close()
    fp.close()

def initFile():
    fp = open("usefullyHouse.txt", "r")
    file = open('hoseLink.txt', 'a+')
    # httpLink = fp.readline()
    # httpLink = httpLink.strip('\n')
    # file.write(str(httpLink) + '\n')
    httpLink = "-1"
    while httpLink != '':
        httpLink = fp.readline()
        httpLink = httpLink.strip('\n')
        requests = req.get(httpLink+'/ershoufang/',headers=headers)
        pattern = re.compile("chengjiao")
        resultList = pattern.findall(requests.text)
        # print(resultList)
        if len(resultList) > 0:
            file.write(str(httpLink) + '\n')
            print(httpLink + "----收录")
        else:
            print(httpLink + "----这条没用")
    fp.close()
    file.close()

def get_html(url,index):
    BaseSpider.random_delay()
    resp = req.get(url, timeout=10, headers=headers)
    html = resp.text
    file = open("xxx.txt",'a+')
    # html = re.sub('\s', '', html)  # 将html文本中非字符数据去掉        
    pattern = re.compile("(\<a href=\")("+"https:\/\/hz.ke.com"+"\/chengjiao\/[a-zA-Z0-9]+\.html)")
    resultList = pattern.findall(html)
    resultList = list(map(lambda x:x[1],resultList))
    print(resultList)
    for i in range(len(resultList)):
        file.write(str(resultList[i]) + '\n')
        print("完成数据收集第" + str(i) + "条")
    file.close()
    return html

if __name__ == '__main__':
    # getListInfo()
    # requests = req.get('https://hz.ke.com/chengjiao/pg1/',timeout=10,headers=headers)
    # print(requests.text)
    # file = open("pg1.txt",'a+')
    # file.write(str(requests.text) + '\n')
    # file.close()
    # 构建全部100个页面url地址
    urls = []
    for i in range(1,2):
        urls.append(f'https://hz.ke.com/chengjiao/cuiyuan/pg{i}/')
        # urls.append(f'https://hz.ke.com/chengjiao/pg{i}/')
 
    print(urls)
    for i in range(len(urls)):
        str = get_html(urls[i],i)
        # print(str)
    print("完成数据收集")
