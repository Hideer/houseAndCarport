#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# read data from csv, write to database
# database includes: mysql/mongodb/excel/json/csv

import os
import re
import json
import pymysql
from lib.utility.path import DATA_PATH
from lib.zone.city import *
from lib.utility.date import *
from lib.utility.version import PYTHON_3
from lib.spider.base_spider import SPIDER_NAME
from lib.oss.download_chenjiao_image import download_upload_oss
from lib.oss.download_chenjiao_image import get_remote_path
from lib.map.map_api import address_to_location
import threading
import threadpool  


pymysql.install_as_MySQLdb()


# def create_prompt_text():
#     city_info = list()
#     num = 0
#     for en_name, ch_name in cities.items():
#         num += 1
#         city_info.append(en_name)
#         city_info.append(": ")
#         city_info.append(ch_name)
#         if num % 4 == 0:
#             city_info.append("\n")
#         else:
#             city_info.append(", ")
#     return 'Which city data do you want to save ?\n' + ''.join(city_info)


if __name__ == '__main__':
    # 设置目标数据库
    ##################################
    # mysql/mongodb/excel/json/csv
    # database = "mysql"
    # database = "mongodb"
    # database = "excel"
    # database = "json"
    database = "mysql"
    ##################################
    db = None
    collection = None
    workbook = None
    csv_file = None
    datas = list()
    thread_xyz = 0
    thread_upload = 0

    if database == "mysql":
        # import records
        # db = records.Database('mysql://root:123456@localhost/wx_duck?charset=utf8')
        db = pymysql.connect(host='localhost',  # 本地数据库
                             user='root',  # 用户名
                             passwd='123456',  # 数据库密码
                             db='wx_duck',  # 数据库名
                             port=3306)   # 数据库编码
    elif database == "mongodb":
        from pymongo import MongoClient
        conn = MongoClient('localhost', 27017)
        db = conn.lianjia  # 连接lianjia数据库，没有则自动创建
        collection = db.xiaoqu  # 使用xiaoqu集合，没有则自动创建
    elif database == "excel":
        import xlsxwriter
        workbook = xlsxwriter.Workbook('xiaoqu.xlsx')
        worksheet = workbook.add_worksheet()
    elif database == "json":
        import json
    elif database == "csv":
        csv_file = open("xiaoqu.csv", "w")
        line = "{0};{1};{2};{3};{4};{5};{6}\n".format('city_ch', 'date', 'district', 'area', 'xiaoqu', 'price', 'sale')
        csv_file.write(line)

    city = get_city('hz')
    # 准备日期信息，爬到的数据存放到日期相关文件夹下
    date = '20230307'
    # date = get_date_string()
    # 获得 csv 文件路径
    # date = "20180331"   # 指定采集数据的日期
    # city = "sh"         # 指定采集数据的城市
    city_ch = get_chinese_city(city)
    csv_dir = "{0}/{1}/ershou_val/{2}/{3}".format(DATA_PATH, SPIDER_NAME, city, date)

    files = list()
    if not os.path.exists(csv_dir):
        print("{0} 不存在.".format(csv_dir))
        print("请先执行 脚本 获取数据")
        print("Bye.")
        exit(0)
    else:
        print('OK, start to process ' + get_chinese_city(city))
    for csv in os.listdir(csv_dir):
        data_csv = csv_dir + "/" + csv
        # print(data_csv)
        files.append(data_csv)

    # 清理数据
    community_count = 0
    house_count = 0
    row = 0
    col = 0
    xiaoqu = []
    fangyuan = []
    cursor = db.cursor()
    t_start = time.time()  # 开始计时

    # 初始化数据库小区数据，生成map字典
    communityMap = {}
    cursor.execute("SELECT * FROM community")
    for row in cursor.fetchall():
        sourceKey = row[1] + ":" + row[2] + ":" + row[3] + ":" + row[4] + ":" + row[5]
        communityMap[sourceKey] = row[0]
    # 初始化数据库房源数据，生成map字典
    houseList = []
    cursor.execute("SELECT `code` FROM house")
    for row in cursor.fetchall():
        houseList.append(row[0])

    for csv in files:
        t_file_start = time.time()
        with open(csv, 'r') as f:
            xiaoqu = []
            xiaoquList = []  
            fangyuan = []
            for line in f:
                text = line.strip()
                try:
                    # 如果小区名里面没有逗号，那么总共是6项
                    if text.count(',') >= 15:
                        date, chinese_district, chinese_area, name, real_price, deal_date, door_model_img, desc_url,code, unit_price, towardAndDecorate_situation, highAndStructure, tax_status, recently_subway, deal_time, original_price = text.split(',')
                    elif text.count(',') < 14:
                        continue
                except Exception as e:
                    print(text)
                    print(e)
                    continue

                toward,decorate_situation = towardAndDecorate_situation.split('|')
                high,structure = highAndStructure.split(' ')

                xiaoquName,door_model,size = re.sub(r" +",' ', name.replace("\n", "").strip()).split(' ')

                # cursor.execute("SELECT * FROM community WHERE name = '%s' AND city = '%s' AND district = '%s' AND area = '%s'" % (xiaoquName,city_ch,chinese_district,chinese_area))
                # comm_results = cursor.fetchone()
                # community_id = comm_results[0] if comm_results else None

                fangyuan_obj = {
                    'date': date,
                    'code': code,
                    'deal_time': deal_time,
                    'deal_date': deal_date,
                    'door_model': door_model,
                    'door_model_img': door_model_img,
                    'desc_url': desc_url,
                    'size': size,
                    'original_price': original_price,
                    'real_price': real_price,
                    'unit_price': unit_price,
                    'toward': toward,
                    'decorate_situation': decorate_situation,
                    'high': high,
                    'structure': structure,
                    'tax_status': tax_status,
                    'recently_subway': recently_subway,
                    # 小区信息
                    'xiaoquName': xiaoquName,
                    'city_ch': city_ch,
                    'chinese_district': chinese_district,
                    'chinese_area': chinese_area
                }
                fangyuan.append(fangyuan_obj)

                xiaoqu_obj = {
                    'province': "",
                    'city': city_ch, 
                    'district': chinese_district, 
                    'area': chinese_area, 
                    'name': xiaoquName, 
                    'logo': ""
                }
                xiaoquKey = xiaoqu_obj['province'] + ":" + xiaoqu_obj['city'] + ":" + xiaoqu_obj['district'] + ":" + xiaoqu_obj['area'] + ":" + xiaoqu_obj['name']
                if xiaoquKey not in xiaoquList:
                    xiaoquList.append(xiaoquKey)
                    xiaoqu.append(xiaoqu_obj)
                   
                # if community_id is None:
                    # xiaoqu.append(xiaoqu_obj)
                    # TODO: 这里暂时只存mysql,此处未结构化
                    # db.query('INSERT INTO community (province, city, district, area, name, logo) '
                    #          'VALUES( :province, :city, :district, :area, :name, :logo)',
                    #          **xiaoqu_obj)
                    
                    # sql = "INSERT INTO community(province, city, district, area, name, logo) VALUES('%s','%s','%s','%s','%s','%s')" % ('',city_ch,chinese_district,chinese_area,xiaoquName,'')
                    # community_id = cursor.execute(sql)
                    # db.commit()

                # 写入mysql数据库
                # if database == "mysql":
                #     cursor.execute("SELECT * FROM house WHERE code = '%s'" % (code))
                #     house_results = cursor.fetchone() or None

                #     if house_results is None:
                #         count += 1
                #         sql = "insert into house(collection_date,code, deal_time,deal_date, door_model, door_model_img, desc_url, size, original_price, real_price, unit_price, toward, decorate_situation, high, structure, tax_status, recently_subway, communityId) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')" % (date,code, deal_time,deal_date, door_model, door_model_img, desc_url, size, original_price, real_price,unit_price, toward, decorate_situation, high, structure, tax_status, recently_subway, community_id)
                #         cursor.execute(sql)
                #         db.commit()
                # # 写入mongodb数据库
                # elif database == "mongodb":
                #     data = dict(city=city_ch, date=date, district=district, area=area, xiaoqu=xiaoqu, price=price,
                #                 sale=sale)
                #     collection.insert(data)
                # elif database == "excel":
                #     if not PYTHON_3:
                #         worksheet.write_string(row, col, unicode(city_ch, 'utf-8'))
                #         worksheet.write_string(row, col + 1, date)
                #         worksheet.write_string(row, col + 2, unicode(district, 'utf-8'))
                #         worksheet.write_string(row, col + 3, unicode(area, 'utf-8'))
                #         worksheet.write_string(row, col + 4, unicode(xiaoqu, 'utf-8'))
                #         worksheet.write_number(row, col + 5, price)
                #         worksheet.write_number(row, col + 6, sale)
                #     else:
                #         worksheet.write_string(row, col, city_ch)
                #         worksheet.write_string(row, col + 1, date)
                #         worksheet.write_string(row, col + 2, district)
                #         worksheet.write_string(row, col + 3, area)
                #         worksheet.write_string(row, col + 4, xiaoqu)
                #         worksheet.write_number(row, col + 5, price)
                #         worksheet.write_number(row, col + 6, sale)
                #     row += 1
                # elif database == "json":
                #     data = dict(city=city_ch, date=date, district=district, area=area, xiaoqu=xiaoqu, price=price,
                #                 sale=sale)
                #     datas.append(data)
                # elif database == "csv":
                #    line = "{0};{1};{2};{3};{4};{5};{6}\n".format(city_ch, date, district, area, xiaoqu, price, sale)
                #    csv_file.write(line)

        # 对比数据库数据获取新增小区数据
        xiaoqu_await_inset = []
        for row in xiaoqu:
            sourceKey = row['province'] + ":" + row['city'] + ":" + row['district'] + ":" + row['area'] + ":" + row['name']
            if sourceKey not in communityMap:
                # 地址解析
                thread_xyz = thread_xyz + 1
                if thread_xyz%5 == 0:
                    time.sleep(1)
                xyz = address_to_location(row['city'] + row['district'] + row['name'])
                row['lng'] = xyz['lng']
                row['lat'] = xyz['lat']
                xiaoqu_await_inset.append(tuple(row.values()))

        # 写入新增的小区信息
        if len(xiaoqu_await_inset):
            community_count += len(xiaoqu_await_inset)
            sql = "INSERT INTO community(province, city, district, area, name, logo, lng, lat) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.executemany(sql,xiaoqu_await_inset)
            db.commit()
            firstInsertId = int(cursor.lastrowid)
            # 更新小区字典
            for inx,row in enumerate(xiaoqu_await_inset):
                sourceKey = row[0] + ":" + row[1] + ":" + row[2] + ":" + row[3] + ":" + row[4]
                communityMap[sourceKey] = firstInsertId + inx

        # 对比数据库获取新增房源数据
        house_await_inset = []
        house_await_inset_img = []
        for row in fangyuan:
            if row['code'] not in houseList:
                sourceKey = ':' + row['city_ch'] + ':' + row['chinese_district'] + ':' + row['chinese_area'] + ':' + row['xiaoquName']
                row['community_id'] = communityMap[sourceKey]
                if row['door_model_img']: 
                    house_await_inset_img.append(row['door_model_img'])
                    row['door_model_img'] = get_remote_path(row['door_model_img'])
                # 删除废弃字段
                del row['city_ch']
                del row['chinese_district']
                del row['chinese_area']
                del row['xiaoquName']
                house_await_inset.append(tuple(row.values()))

        # 写入新增的房源信息
        if len(house_await_inset):
            # 户型图上传oss
            print('需上传图片数:',len(house_await_inset))
            pool_size = 180 if len(house_await_inset_img) >=200 else len(house_await_inset_img)
            pool = threadpool.ThreadPool(pool_size) 
            requests = threadpool.makeRequests(download_upload_oss, house_await_inset_img) 
            [pool.putRequest(req) for req in requests]
            pool.wait()
            pool.dismissWorkers(pool_size, do_join=True)  # 完成后退出
            # download_upload_oss(row['door_model_img'])

            house_count += len(house_await_inset)
            sql = "INSERT INTO house(collection_date,code, deal_time,deal_date, door_model, door_model_img, desc_url, size, original_price, real_price, unit_price, toward, decorate_situation, high, structure, tax_status, recently_subway, communityId) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.executemany(sql, house_await_inset)
            xxx345 = cursor.fetchall()
            db.commit()

            # 更新已存入房源编码
            for row in house_await_inset:
                houseList.append(row[1])

        t_file_end = time.time()

        print("{0} 已写入完成, 耗时 {1}".format(csv, t_file_end-t_file_start))
    #  写入，并且关闭句柄
    if database == "excel":
        workbook.close()
    elif database == "json":
        json.dump(datas, open('xiaoqu.json', 'w'), ensure_ascii=False, indent=2)
    elif database == "csv":
        csv_file.close()
    elif database == "mysql":
        cursor.close()
        db.close()

    # 计时结束，统计结果
    t_end = time.time()

    print("新增写入 {0} 条小区信息, {1} 条房源信息. 总耗时: {2}s".format(community_count, house_count, t_end - t_start))
