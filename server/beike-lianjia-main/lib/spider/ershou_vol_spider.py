#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# 爬取二手房成交数据的爬虫派生类

import re
import threadpool
from bs4 import BeautifulSoup
from lib.item.changjiao import *
from lib.zone.city import get_city
from lib.spider.base_spider import *
from lib.utility.date import *
from lib.utility.path import *
from lib.zone.area import *
from lib.utility.log import *
import lib.utility.version


class ErShouVolSpider(BaseSpider):
    def collect_area_ershou_data(self, city_name, area_name, fmt="csv"):
        """
        对于每个板块,获得这个板块下所有二手房成交的信息
        并且将这些信息写入文件保存
        :param city_name: 城市
        :param area_name: 板块
        :param fmt: 保存文件格式
        :return: None
        """
        district_name = area_dict.get(area_name, "")
        csv_file = self.today_path + "/{0}_{1}.csv".format(district_name, area_name)
        with open(csv_file, "w") as f:
            # 开始获得需要的板块数据
            ershous = self.get_area_ershou_info(city_name, area_name)
            # 锁定，多线程读写
            # TODO:这里的锁和线程联动没明白？
            if self.mutex.acquire(1):
                self.total_num += len(ershous)
                # 释放
                self.mutex.release()
            if fmt == "csv":
                for ershou in ershous:
                    # print(date_string + "," + xiaoqu.text())
                    f.write(self.date_string + "," + ershou.text() + "\n")
        time.sleep(random.randint(1, 6))
        print("Finish crawl area: " + area_name + ", save data to : " + csv_file)

    @staticmethod
    def get_area_ershou_info(city_name, area_name):
        """
        通过爬取页面获得城市指定版块的二手房成交信息
        :param city_name: 城市
        :param area_name: 版块
        :return: 二手房数据列表
        """
        total_page = 1
        district_name = area_dict.get(area_name, "")
        # 中文区县
        chinese_district = get_chinese_district(district_name)
        # 中文版块
        chinese_area = chinese_area_dict.get(area_name, "")

        ershou_list = list()
        page = 'https://{0}.{1}.com/chengjiao/{2}/'.format(city_name, SPIDER_NAME, area_name)
        print(page)  # 打印版块页面地址
        headers = create_headers()
        response = requests.get(page, timeout=10, headers=headers)
        html = response.content
        soup = BeautifulSoup(html, "lxml")

        # 获得总的页数，通过查找总页码的元素信息
        try:
            page_box = soup.find_all('div', class_='page-box')[0]
            matches = re.search('.*"totalPage":(\d+),.*', str(page_box))
            total_page = int(matches.group(1))
        except Exception as e:
            print("\t警告: only find {1} page for {0} in {2}".format(area_name, total_page, page))
            # print('\t抓取页面内容:'+response.text)
            print(e)

        # 从第一页开始,一直遍历到最后一页
        for num in range(1, total_page + 1):
            page = 'https://{0}.{1}.com/chengjiao/{2}/pg{3}/'.format(city_name, SPIDER_NAME, area_name, num)
            print(page)  # 打印每一页的地址
            headers = create_headers()
            BaseSpider.random_delay()
            response = requests.get(page, timeout=10, headers=headers)
            html = response.content
            soup = BeautifulSoup(html, "lxml")

            # 获得有小区信息的panel
            house_panel = soup.find('ul', class_="listContent")
            if house_panel:
                house_elements = house_panel.find_all('li')
                for house_elem in house_elements:
                    name = house_elem.find('div', class_='title')
                    desc_url = name.find('a')
                    price = house_elem.find('div', class_="totalPrice")
                    unit_price = house_elem.find('div', class_="unitPrice")
                    date = house_elem.find('div', class_="dealDate")
                    pic = house_elem.find('a', class_="img").find('img', class_="lj-lazy")
                    desc_info = house_elem.find('div', class_="houseInfo")
                    desc_position = house_elem.find('div', class_="positionInfo")
                    desc_deal_house = house_elem.find('span', class_="dealHouseTxt").find_all('span') if house_elem.find('span', class_="dealHouseTxt") else None
                    desc_deal_cycle = house_elem.find('span', class_="dealCycleTxt").find_all('span') if house_elem.find('span', class_="dealCycleTxt") else None

                    # 继续清理数据
                    desc_url = desc_url.get('href','').strip()
                    name = re.sub(r" +",' ', name.text.replace("\n", "").strip()).replace(",", "-")
                    price = re.sub(r" +",' ', price.text.replace("\n", "").strip())
                    date = date.text.strip()
                    unit_price = re.sub(r" +",' ', unit_price.text.replace("\n", "").strip())
                    # pic 标签可能不存在
                    pic = pic.get('data-original','').strip() if pic else ''
                    desc_info = desc_info.text.replace("\n", "").strip()
                    desc_position = re.sub(r" +",' ', desc_position.text.replace("\n", "").strip())
                    trade_mark = str(desc_url.split('/')[-1].replace(".html",""))
                    desc_tax = ''
                    desc_dist = ''
                    desc_cycle = ''
                    desc_original_price = ''
                    if desc_deal_house:
                        if len(desc_deal_house)>1:
                            desc_tax = desc_deal_house[0].text.strip()
                            desc_dist = desc_deal_house[1].text.strip()
                        elif '房屋' in desc_deal_house[0].text:
                            desc_tax = desc_deal_house[0].text.strip()
                        else:
                            desc_dist = desc_deal_house[0].text.strip()
                    if desc_deal_cycle:
                        if len(desc_deal_cycle)>1:
                            desc_original_price = desc_deal_cycle[0].text.strip()
                            desc_cycle = desc_deal_cycle[1].text.strip()
                        elif '挂牌' in desc_deal_cycle[0].text:
                            desc_original_price = desc_deal_cycle[0].text.strip()
                        else:
                            desc_cycle = desc_deal_cycle[0].text.strip()

                    # 作为对象保存
                    ershou = ChengJiao(chinese_district, chinese_area, name, price, date, unit_price, desc_url, pic, trade_mark, desc_info, desc_position,desc_tax, desc_dist, desc_cycle, desc_original_price)
                    ershou_list.append(ershou)
        return ershou_list

    def start(self):
        city = 'hz' or get_city()
        self.today_path = create_date_path("{0}/ershou_val".format(SPIDER_NAME), city, self.date_string)

        t1 = time.time()  # 开始计时

        # 获得城市有多少区列表, district: 区县
        districts = get_districts(city)
        print('City: {0}'.format(city))
        print('Districts: {0}'.format(districts))

        # 获得每个区的板块, area: 板块
        areas = list()
        for district in districts:
            areas_of_district = get_areas(city, district)
            print('{0}: Area list:  {1}'.format(district, areas_of_district))

            if areas_of_district is not None:
                # 用list的extend方法,L1.extend(L2)，该方法将参数L2的全部元素添加到L1的尾部
                areas.extend(areas_of_district)
                # 使用一个字典来存储区县和板块的对应关系, 例如{'cuiyuan': 'xihu', }
                for area in areas_of_district:
                    area_dict[area] = district      
        print("Area:", areas)
        print("District and areas:", area_dict)

        # 准备线程池用到的参数
        nones = [None for i in range(len(areas))]
        city_list = [city for i in range(len(areas))]
        # zip 将可迭代的元素作为参数，对象中的元素打包成元祖，并将元祖组成列表 https://www.runoob.com/python/python-func-zip.html
        # args = zip(zip(['hz'], ['cuiyuan']), nones)
        args = zip(zip(city_list, areas), nones)
        # areas = areas[0: 1]   # For debugging

        # 针对每个板块写一个文件,启动一个线程来操作
        pool_size = thread_pool_size
        # 多线程提高效率，args 的长度就是需要循环的次数 pool_size 控制线程数 https://www.cnblogs.com/xiaozi/p/6182990.html
        pool = threadpool.ThreadPool(pool_size)
        my_requests = threadpool.makeRequests(self.collect_area_ershou_data, args)
        [pool.putRequest(req) for req in my_requests]
        pool.wait()
        pool.dismissWorkers(pool_size, do_join=True)  # 完成后退出

        # 计时结束，统计结果
        t2 = time.time()
        print("Total crawl {0} areas.".format(len(areas)))
        print("Total cost {0} second to crawl {1} data items.".format(t2 - t1, self.total_num))


if __name__ == '__main__':
    pass
