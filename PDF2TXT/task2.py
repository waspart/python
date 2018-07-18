# BASE64编码解码

import base64

if __name__ == '__main__':
	a = 'this is a string'.encode('utf-8')
	print(a)

	enstr = base64.b64encode(a) #编码
	print(enstr)
	enstr_clear = str(enstr, 'utf-8')
	print(enstr_clear)  # 将编码结果中的b''去掉

	destr = base64.b64decode(enstr_clear) # 解码
	print(destr) 
	destr_clear = str(destr, 'utf-8')
	print(destr_clear)


