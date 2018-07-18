# 将一个字符串写入TXT文件

s1 = '我是一个字符串'
s2 = 'I am a string'

f = open("D:/python/PDF2TXT/file/test.txt", "a+")
f.write(repr(s1) + '\n')
f.write(s2)

f.close()

print(type(eval("{'name':'ljq', 'age':24}")))

d = {'name':'Zara', 'age':7, 'class':'first'}
print(type(str(d)))
print(d)
print(bytes(str(d), encoding='utf-8'))