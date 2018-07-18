# json字符串解码与编码

import json

with open('D:/python/PDF2TXT/file/test4.txt') as fin:
    a = fin.read()
	#print(fin.read())
data = json.loads(a)  # 解码为dict类型
#print("data['name']:", data['name'])
print(type(data))
print(data)

jdata = json.dumps(data) # 编码为json格式
print(type(jdata))
print(jdata)
print(jdata.encode('utf-8'))

print(json.loads(jdata))


print(len(data))
print('遍历元素：')
for item in data.items():
	print(item)
print('遍历键：')
for key in data.keys():
	print(key)

print('遍历值：')
for val in data.values():
	print(val)
	print(type(val))

print('\n\n获取结果：')
iitems = data["items"]
for it in iitems:
	print(it['itemstring'])


