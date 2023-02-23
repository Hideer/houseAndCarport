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
    headers["Cookie"] = "SECKEY_ABVK=nQYk1Jpn7q8U08iDBjTdqdN2ooAFIwaAw1Qd/FxFBjs%3D; BMAP_SECKEY=nkvAt5QlUwhHgkkgqKOqOkO2Wyx3HYsDSmQJ5Tgy1Uvjtd3sVCHpK8_blH-L2L00qPZfb0tyDUIOTn43-lZ48BPRxgmn1mE00dEAyp-BWJwAaRn0Oiccm3JwEX9bGWvz894k9YtSr1GIqoxSz2EZrwmJdRAQUh7NRRn8U_uZJ0nfxEPfPQJ8fjrnsqZkJM2P; lianjia_uuid=ad89a543-48c8-4d36-876d-28d3abc7878c; Hm_lvt_9152f8221cb6243a53c83b956842be8a=1676966895; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218673042936d5a-01491bd4cebb17-1f525634-1296000-18673042937dbe%22%2C%22%24device_id%22%3A%2218673042936d5a-01491bd4cebb17-1f525634-1296000-18673042937dbe%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; beikeBaseData=%7B%22parentSceneId%22%3A%22%22%7D; crosSdkDT2019DeviceId=-7y9013--scnacd-b219ffsqhyml5de-o4olx0x7w; select_city=330100; lianjia_ssid=477099f4-5f6e-4d40-af51-9ea5e0e4f6a3; login_ucid=2000000025257194; lianjia_token=2.00139f201d6b87291b0232092c1fd93035; lianjia_token_secure=2.00139f201d6b87291b0232092c1fd93035; security_ticket=LJOx8wE5uO9C6nu3KJzT7QxCHZccjBObnLvRxzARsD9zrfWAuMHlMu8w31q6nVlvfl8ZGklSz1LmQUV/D+OH3ufrx6FnfnBS25iOzsZyvcW8EniU5KtSSx5oxUnShLzhiTggGtdFFJdGvkNjm3yvoLNytYt4TlWtlj+ITSnw64U=; Hm_lpvt_9152f8221cb6243a53c83b956842be8a=1677073060; srcid=eyJ0Ijoie1wiZGF0YVwiOlwiYjhjMTg1YmFmZjJkNGMwNTYwNmFiYzY3MDg3NGE1NjgzODI0MWY1M2JmZGU0YzJmNjBjOTE5YzRiMTM5M2Q5M2Q2MWQzOTI0MWE2MGJhYmVmNTI2MGI1ODc1NTgxNWNiYzFlY2Y5MTNiOWQyYmIwYTUxOTVhNmE3Mzg4YmI3NjMyZjQzMmNlYjliYTBmNWNiZmJjZjBiMzZlMWM1YjU1ZmZkMGUyMWI2MmE0YmRjNzc5NzVkYjI2YWY4NjE4YThkYmUzNmUxOTc2YmVmYzE2YjYzMDczMjU2YWY4NGY2N2NkMmI4MDA0YjRlZDc0Nzk5ZDk2NzhiZTJmYjNjMjY1NVwiLFwia2V5X2lkXCI6XCIxXCIsXCJzaWduXCI6XCJlYjlkZDc4YlwifSIsInIiOiJodHRwczovL2h6LmtlLmNvbS9jaGVuZ2ppYW8vY3VpeXVhbi8iLCJvcyI6IndlYiIsInYiOiIwLjEifQ=="
    return headers


if __name__ == '__main__':
    pass
