import cv2
import os
import requests
import upyun
import numpy as np
from PIL import Image
from itertools import product

up = None
local_image_prefix = './data/image/'

# 将网图下载到本地
def download_image(url):
    fileName = ((url.split('/')[-1]).split('?')[0]).replace('.280x210.jpg','')
    url = url.replace('.280x210.jpg?from=ke.com', '!m_fill,w_210,h_164,f_jpg')
    file = requests.get(url)
    path = local_image_prefix + fileName
    with open(path, 'wb') as f:
        f.write(file.content) 
    return {'fileName':fileName, 'localPath':path}


# 图片上传oss
def upload_oss(path,file_name):
    global up
    if up is None:
        up = upyun.UpYun('house-door-model', username='haojiubujian123', password='22OUmk2coVzAlRRuCkjuTUiImrBzymzI')
    headers = {'x-gmkerl-rotate': '180'}
    with open(path, 'rb') as f:
        up.put('/' + file_name, f, checksum=True, headers=headers)

# 去水印（暂时不需要，找到了无水印图片）
def remove_watermark(file_info):
    path = file_info['localPath']
    newPath = local_image_prefix + 'no_watermark.' + file_info['fileName']

    img = Image.open(path)
    width, height = img.size

    img=cv2.imread(path,1)
    hight,width,depth=img.shape[0:3]

    # 截取
    cropped = img[int(hight*0.40):int(hight*0.60), int(width*0.35):int(width*0.65)]  # 裁剪坐标为[y0:y1, x0:x1]
    cv2.imwrite(newPath, cropped)
    imgSY = cv2.imread(newPath,1)

    # 204, 218, 240
    # 205, 212, 224
    # 209, 215, 223
    # 200, 209, 236
    # # 图片二值化处理，把[200,200,200]-[250,250,250]以外的颜色变成0
    thresh = cv2.inRange(imgSY,np.array([0, 0, 0]),np.array([204, 218, 240]))
    cv2.imwrite(newPath, thresh)

    # 创建形状和尺寸的结构元素
    kernel = np.ones((3,3),np.uint8)
    # 扩展待修复区域
    hi_mask = cv2.dilate(thresh,kernel,iterations=2)
    specular = cv2.inpaint(imgSY,hi_mask,5,flags=cv2.INPAINT_TELEA)
    cv2.imwrite(newPath, specular)

    # 覆盖图片
    imgSY = Image.open(newPath)
    img = Image.open(path)
    img.paste(imgSY, (int(width*0.35),int(hight*0.40),int(width*0.65),int(hight*0.60)))
    img.save(newPath)



if __name__ == "__main__":
    file_info = download_image('https://ke-image.ljcdn.com/hdic-frame/standard_8035318b-0c2e-44d0-84a3-d43e25e11ff9.png.280x210.jpg?from=ke.com')
    print(file_info)
    # remove_watermark(file_info)
    upload_oss(file_info['localPath'],file_info['fileName'])

# https://ke-image.ljcdn.com/hdic-frame/standard_82994960-0970-4ee9-9396-5831d5196c21.png.280x210.jpg?from=ke.com
# https://ke-image.ljcdn.com/hdic-frame/standard_82994960-0970-4ee9-9396-5831d5196c21.png!m_fill,w_210,h_164,f_jpg?from=ke.com