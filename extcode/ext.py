import sys
import io
import os
import time
from aip import AipOcr
from charJ import ext_non_char


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 百度OCR接口信息
# 公司账号信息
app_id = '11073548'
api_key = 'rLlHa7cqVnvhNTEc3PQlEigi'
secret_key = 'sAySyzixGPUemPSQ9S17YYBRW7a7SdX1'

# 个人账号信息
# app_id = '11073460'
# api_key = 'qaL43FdLsGUjLNxgzvcpXLwP'
# secret_key = '3Crcl3VHrSMC1yIIBS75wyjTGZco9BwS'

client = AipOcr(app_id, api_key, secret_key)

img_path = 'imgs/'
save_path = 'txts/'
# len(os.listdir(img_path))
for i in list(range(len(os.listdir(img_path)))):
    # print('page' + repr(i) + '.jpg')
    all_cont = ''
    img = 'page' + repr(i) + '.jpg'
    # print(img_path + img)
    image = get_file_content(img_path + img)

    ret = client.basicGeneral(image)
    list_dct = ret['words_result']

    for d in list_dct:
        s_part = d['words']
        res = ext_non_char(s_part)
        if res != '':
            all_cont = all_cont + ext_non_char(s_part)
    # print(all_cont)

    txt = save_path + 'page' + repr(i) + '.txt'
    with open(txt, 'ab+') as fsave:
        fsave.write(bytes(all_cont, encoding='utf-8'))

    print(img + '\t Done!!!')
    # print("################\n")
    # time.sleep(1)
