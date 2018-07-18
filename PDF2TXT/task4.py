# 图片base64编码

import base64

with open(r'D:\python\PDF2TXT\img\tnb.bmp', 'rb') as fin:
	data = fin.read()
	enstr = base64.b64encode(data)
	print(str(enstr, 'utf-8'))
