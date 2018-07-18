# 調用百度OCR接口
from aip import AipOcr
import json

app_id = '11073460'
api_key = 'qaL43FdLsGUjLNxgzvcpXLwP'
secret_key = '3Crcl3VHrSMC1yIIBS75wyjTGZco9BwS'

client = AipOcr(app_id, api_key, secret_key)


def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


image = get_file_content('tnb.bmp')
ret = client.basicGeneral(image)

print(type(ret))
print(ret)

fj = open('file/json.txt')
fj.write(json.dumps(ret))
fj.close()


# options = {}
# options['language_type'] = 'CHN_ENG'
# options['detect_direction'] = 'true'
# options['detect_language'] = 'true'
# options['probability'] = 'true'
