#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 此代码仅供学习与交流，请勿用于商业用途。
# USER AGENTS 可以自己添加

import random
from lib.spider.base_spider import SPIDER_NAME

USER_AGENTS = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
]


def create_headers():
    headers = dict()
    headers["User-Agent"] = random.choice(USER_AGENTS)
    headers["Referer"] = "https://clogin.ke.com/"
    # headers["Referer"] = "http://www.{0}.com".format(SPIDER_NAME)
    headers["Cookie"] = "SECKEY_ABVK=l42vNpAFyfz01cReqIEU4VptLNJ3kGh4GAbjrCxkd94%3D; BMAP_SECKEY=l42vNpAFyfz01cReqIEU4eV09r6nrGWr_gGQBdfPKxlAee5lti0RDaHLU9OsvZV3TI_U2o39erzcalC7WXbIv3tVSYpaStA7RAPt43f45Cmv6ZG1Yw6_Q0xcLzgrXoR59PNFt6Rr7wYot8-W-w1e0q4Y14xrszKzLOVlzfuGm_OPgxgR_EwOYArQnCGbXCpN; lianjia_uuid=ad89a543-48c8-4d36-876d-28d3abc7878c; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1676966895; beikeBaseData=%7B%22parentSceneId%22%3A%22%22%7D; crosSdkDT2019DeviceId=-7y9013--scnacd-b219ffsqhyml5de-o4olx0x7w; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1677565423; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218673042936d5a-01491bd4cebb17-1f525634-1296000-18673042937dbe%22%2C%22%24device_id%22%3A%2218673042936d5a-01491bd4cebb17-1f525634-1296000-18673042937dbe%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.google.com.hk%2F%22%2C%22%24latest_referrer_host%22%3A%22www.google.com.hk%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%7D%7D; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiMDhmMDk5YTA3OTE0Y2Y2MGE5Zjk2MWQ0ZGMyMjU2MDQ5OWQ3MTY2YWNkNmEzYTU4NzIzYWJmNGZlMWVjOWQ3ZDI2MzY1YjM2NjdhZjZkOTU2OWY1Y2YyYzNkZjA4YjAzNzc2ZTEzZTQ0NjdiMjliMmY2MTE5YmJkYTIxYmEzNzRiMGNkMzE4NGViMTBjMmMzZjNjOGViODg5OGRhZWQ4NWMyZDYwOWFkOGI5MDRlMWFlMmY2N2IzMTI5MWUyYWZiNGM5ZTQyYjAyNDVlZTU1MDNiMGExYmZkY2Y2NGMyYzc1NTkzYjcwMGU3MTMzY2ZiNjkyMTY3NzFjZDhmZmM5MlwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCI2NDY1MGVhZlwifSIsInIiOiJodHRwczovL2h6LmtlLmNvbS94aWFvcXUvMTgyMDAyNzg3Mjg5MTY0MC8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ==; select_city=330100; lianjia_ssid=2dc59449-c545-4338-9cd0-458c1dcf1316; login_ucid=2000000025257194; lianjia_token=2.001477ac026c6fa50405da85338eb15fd8; lianjia_token_secure=2.001477ac026c6fa50405da85338eb15fd8; security_ticket=O7usCqdTl9W3t5EcDTt2Mm9iX8Nn0BM6myC4LwCkFP3IwaT7LU9KMbzl3s36syQwy0zf9ajpFk7G0ytmOHL5Le07ZV3jmhmwnZl29Q0QBjPknGjJQeYzntqpYWinYk7vTIRY9HCreLalyyGBBfcnl6gM+H4fgYp1FR7H3wsEWbA="
    return headers


if __name__ == '__main__':
    pass
