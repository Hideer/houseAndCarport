#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import requests as req
import json
import re
from fake_useragent import UserAgent
# from lib.spider.base_spider import SPIDER_NAME

# 此平台需要登录
# s = req.Session()
headers = {
    "Cookie": "SECKEY_ABVK=nQYk1Jpn7q8U08iDBjTdqfj70DqI6vcJ0SrYvFQDSAQ%3D; BMAP_SECKEY=nkvAt5QlUwhHgkkgqKOqOnVP9-YAEkVm4YocmiNquOxytQpqLbOnaaKwOrVzCCOpYFZLLRw_PXhBrdLsMRRPDAa349ovZ7Xj70zVezuxRxuzPJP_SnxKXyCe5RsL6wiZoD8Gp2w0UkfmH9buzwrsOoHN9Z4ei3qVIGjJysu5mUqbTGScO6x_y4mVyfhLqs4E; lianjia_uuid=ad89a543-48c8-4d36-876d-28d3abc7878c; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1676966895; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218673042936d5a-01491bd4cebb17-1f525634-1296000-18673042937dbe%22%2C%22%24device_id%22%3A%2218673042936d5a-01491bd4cebb17-1f525634-1296000-18673042937dbe%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; beikeBaseData=%7B%22parentSceneId%22%3A%22%22%7D; crosSdkDT2019DeviceId=-7y9013--scnacd-b219ffsqhyml5de-o4olx0x7w; lianjia_ssid=bbea17eb-d0b6-4041-9713-4f5e23d626fb; select_city=330100; login_ucid=2000000025257194; lianjia_token=2.0010fff2f168e7fbf70152dbc0b5e8adce; lianjia_token_secure=2.0010fff2f168e7fbf70152dbc0b5e8adce; security_ticket=rdUvGUHvhu/XMEQ4l+KwpaBNV/+60lia+eSwU/ALcRlS+/uCa0rWOwRvrKtW98Yi++lOExVE5grYYoMwzo2G39oMvnl4Ns91KGGNhYojbr8rPha1weE54o9h3PgNfOcjyzJc0fm9Lw56vVEaI7WTukJVbIuEVrywIzPJbDXrxr8=; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1676988913; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiNWEyYzBmYmFhNmU3NTIzYTQzNjU5NzI4YmZmODQxNTFhYmJmZjdmMWY5MGY5YjQyODlkYThkY2M5MTFlNjg1MjcxNDI2ZmE1YjkyMDljNGRhZTk0YThlYmUyYzA4ZjFlNmM0ZGJmOWQyYzM1YmRiZmEyNjg4MjA1NGQ3NDUyOGUzMjQ1MDg2ZjRiMDZlMzRjNWQ5NDg1ZWRiM2Y3OGVjNjk1ODY5MGYyMGU2Y2JjMGYxYTM5NmRmYmU4MTYxNzQ5NTA2Yzc4MTQ2ZjMxYTgzY2I2MTg0MTU1NWY4OTA5NGMzM2U5NTU3MWQxYmRkYzNmNjA4MTA0YWZlMDg4NzhjN1wiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI1YjhiY2E2NVwifSIsInIiOiJodHRwczovL2h6LmtlLmNvbS9jaGVuZ2ppYW8vcGcxLyIsIm9zIjoid2ViIiwidiI6IjAuMSJ9",
    'User-Agent': UserAgent().random,  # 使用第三方库生成的随机UA
    # "Accept-Encoding": "gzip, deflate, br"
    # 'Referer': 'https://clogin.ke.com/'
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
            # BaseSpider.random_delay()
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


def analysis(url,file):
    print(1111)

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
        # analysis(httpLink, file)
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

def analysisCity():
    # file = open('usefullyHouse.txt', 'a+')
    # city_name: '[\u4e00-\u9fa5]+
    requests = req.get("https://hf.ke.com")
    # pattern = re.compile("\<a  class=\"\" href=\"" + httpLink + "\/ershoufang\/\" \>二手房")

def get_html(url):
    print(url)
    resp = req.get(url, headers=headers)
    html = resp.text
    html = re.sub('\s', '', html)  # 将html文本中非字符数据去掉        
          
    return html
if __name__ == '__main__':
    getListInfo()
    # 构建全部100个页面url地址
    # urls = []
    # for i in range(1,10):
    #     urls.append(f'https://hz.ke.com/chengjiao/pg{i}/')
    # for i in range(len(urls)):
    #     str = get_html(urls[i])
    #     print(str)

    print("完成数据收集")
