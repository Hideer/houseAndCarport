import time
import requests

developer_key = 'K7ZBZ-XJY6U-3IZVA-BNMJY-7UGCO-NFFZM'  # 开发者key
# Post请求测试
def address_to_location(address):
    # 腾讯位置服务的并发: 5次/秒/接口/Key
    # 日调用量：10,000次/接口/Key
    parameters = {'address': address, 'key': developer_key}
    base = "http://apis.map.qq.com/ws/geocoder/v1/?"
    try:
        response = requests.get(base, parameters)
        answer = response.json()
        if answer['status'] == 0:
            # answer['result']['location']
            return {'lng':answer['result']['location']['lng'], 'lat': answer['result']['location']['lat']}
        else:
            raise Exception(answer)
    except Exception as e:
        print('地址解析错误: {0}--{1}'.format(address, e))
        return {'lng': '', 'lat': ''}


# Get请求测试
def address_coordinate_get_request(location):
    parameters = {'location': location, 'key': developer_key}
    parameters = {}
    base = 'http://apis.map.qq.com/ws/geocoder/v1/?'  # 地址解析，地址转坐标
    base = "http://apis.map.qq.com/ws/place/v1/search?" + \
           "boundary=region(武汉,0)&keyword=酒店&page_size=20&page_index=1&orderby=_distance&key=" + \
           developer_key  # 腾讯地图地点搜索
    response = requests.get(base, parameters)
    response.encoding = 'utf-8'
    answer = response.json()
    print(answer['data'][0]['category'])


if __name__ == '__main__':
    start = time.time()
    print("Start: " + str(start))
    print('广东省广州市天河区天河路600号')
    address_coordinate_get_request('39.984154,116.307490')
    address_coordinate_post_request("广东省广州市天河区天河路600号")

    stop = time.time()
    print("Stop: " + str(stop))
    print(str(stop - start) + "秒")
