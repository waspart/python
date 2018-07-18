# 图片已经提取成功的前提下，调用百度OCR接口，识别所有图片中的文字

import os
from aip import AipOcr

# 公司账号信息
app_id = '11073548'
api_key = 'rLlHa7cqVnvhNTEc3PQlEigi'
secret_key = 'sAySyzixGPUemPSQ9S17YYBRW7a7SdX1'

# 个人账号信息
# app_id = '11073460'
# api_key = 'qaL43FdLsGUjLNxgzvcpXLwP'
# secret_key = '3Crcl3VHrSMC1yIIBS75wyjTGZco9BwS'

client = AipOcr(app_id, api_key, secret_key)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


# image = get_file_content('tnb.bmp')
# ret = client.basicGeneral(image)

_path = 'images/'
count = 0
ret = {}
for i in list(range(3161, 4000, 2)):
    filename = 'page-' + repr(i) + '.png'
    # print('processing', filename, end="  ")
    if os.path.isfile(_path + filename):
        image = get_file_content(_path + filename)
        ret = client.basicGeneral(image)
        # print(repr((i + 1) / 2), '正处理：', filename)
        # print(ret)
        count += 1
        print(repr(count), 'processing', filename, end="  ")

        list_dct = ret['words_result']

        for d in list_dct:
            s_part = d['words']
            f = open('mk2.txt', 'a+')
            f.write(s_part)
            f.close()
        print('Done!!!!!!!!')

print('\n################################')
print('#### 共处理文件总数量：', count, '####')
print('################################')
