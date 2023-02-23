#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup
from lib.item.changjiao import *
import json
import re
from fake_useragent import UserAgent
from lib.spider.base_spider import BaseSpider

if __name__ == '__main__':
    # response = requests.get('./pg1.html', timeout=10)
    # html = response.content
    print(''.find_all('span'))
    pass
    soup = BeautifulSoup(open('pg1.html'), "lxml")

    ershou_list = list()
    # 获得有小区信息的panel
    house_panel = soup.find('ul', class_="listContent")
    house_elements = house_panel.find_all('li')
    num = 0
    for house_elem in house_elements:
        name = house_elem.find('div', class_='title')
        desc_url = name.find('a')
        price = house_elem.find('div', class_="totalPrice")
        unit_price = house_elem.find('div', class_="unitPrice")
        date = house_elem.find('div', class_="dealDate")
        pic = house_elem.find('a', class_="img").find('img', class_="lj-lazy")
        desc_info = house_elem.find('div', class_="houseInfo")
        desc_position = house_elem.find('div', class_="positionInfo")
        desc_deal_house = house_elem.find('span', class_="dealHouseTxt").find_all('span')
        desc_deal_cycle = house_elem.find('span', class_="dealCycleTxt").find_all('span')

        num = num + 1

        # 继续清理数据
        desc_url = desc_url.get('href','').strip()
        name = name.text.replace("\n", "")
        price = re.sub(r" +",' ', price.text.replace("\n", "").strip())
        date = date.text.strip()
        unit_price = re.sub(r" +",' ', unit_price.text.replace("\n", "").strip())
        # pic 标签可能不存在
        pic = pic.get('data-original','').strip() if pic else ''
        desc_info = desc_info.text.replace("\n", "").strip()
        desc_position = desc_position.text.replace("\n", "").strip()
        desc_tax = desc_deal_house[0].text.strip() if len(desc_deal_house)>1 else ''
        desc_dist = desc_deal_house[1].text.strip() if len(desc_deal_house)>1 else desc_deal_house[0].text.strip()
        desc_cycle = desc_deal_cycle[1].text.strip() if len(desc_deal_cycle)>1 else desc_deal_house[0].text.strip()
        desc_original_price = desc_deal_cycle[0].text.strip() if len(desc_deal_cycle)>1 else ''
        trade_mark = desc_url.split('/')[-1].replace(".html","")

        # 作为对象保存
        ershou = ChengJiao('chinese_district', 'chinese_area', name, price, unit_price, desc_url, pic, trade_mark, desc_info, desc_position,desc_tax, desc_dist, desc_cycle, desc_original_price)
        # print('chinese_district', 'chinese_area', trade_mark, name, price, unit_price, desc_url, pic, desc_info, desc_position,desc_tax, desc_dist, desc_cycle, desc_original_price)
        ershou_list.append(ershou)
    print('over~')
