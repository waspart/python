# 腾讯优图接口识别图片中的文字
import base64
import TencentYoutuyun
import sys, io
import json

#sys.stdout = io.TestIOWrapper(sys.stdout.buffer, encoding='gb2312')

url = 'https://api.youtu.qq.com/youtu/ocrapi/generalocr'
appid = '10125301'
secretID = 'AKID89zmOpEC9uTr39MnJguwGPRIxTq1inQr'
secretKey = 'OeiaGAtRnxyrdDdszueWEBmJfsvnV1LT'
userid = '981466423'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
#image_code = ''


#with open(r'D:\python\PDF2TXT\img\tnb.bmp', 'rb') as fin:
	#data = fin.read()
	#image_code = str(base64.b64encode(data), 'utf-8')
	#print(str(enstr, 'utf-8'))

youtu = TencentYoutuyun.YouTu(appid, secretID, secretKey, userid, end_point)
# print(type(youtu))

ret = youtu.generalocr(r'img2.png', data_type = 0)
# print(type(ret))
# print(ret['items'][0]['itemstring'].encode('iso-8859-1').decode('GB18030'))
# print(ret['items'][0]['itemstring'].encode('iso-8859-1').decode('GB2312'))
# print(ret['items'][0]['itemstring'].encode('iso-8859-1').decode('GBk'))
# print(ret['items'][0]['itemstring'].encode('iso-8859-1').decode('UTF-8'))
# print(ret['items'][1]['itemstring'].encode('iso-8859-1').decode('UTF-8'))
# print(ret['items'][2]['itemstring'].encode('iso-8859-1').decode('UTF-8'))
print(ret)
for i in list(range(len(ret['items']))):
	print(ret['items'][i]['itemstring'].encode('iso-8859-1').decode('UTF-8'))


# d = json.dumps(ret)
# print(d)
# print(d.encode('GB18030'))

# f4 = open("D:/python/PDF2TXT/file/test4.txt", "w")
# f4.write(d)
# f4.close()

