# import unicode
import os
from wand.image import Image
import PyPDF2

s1 = r"{'character': 'å\x89\x8d', 'confidence': 0.9997631907463074}, {'character': 'è¨\x80', 'confidence': 0.9992035031318665}], 'candword': [], 'parag': {'word_size': 70, 'parag_no': 0}}"
print(s1)
# print(unicode(s1, 'utf-8'))

s2 = '汉字'
print(s2)

print('a' == '\u0061')
print(b'\xc2\xbb'.decode('utf-8'))
print('\u00bb')

_path = r'D:\python\PDF2TXT'
lst = os.listdir(_path)
for ls in lst:
    if os.path.isfile(_path + '\\' + ls):
        print(ls + ' is a file')
    else:
        print(ls + ' is not a file')
# for f in os.walk(_path):
# print(f)

print(os.path.abspath('.'))
print(os.path.abspath('..'))

s3 = r'img-1.png'
lst_s3 = s3.split('.')
print(lst_s3)

f3 = open('file/test.txt', 'a+')
f3.write('i am a test')
f3.close()

s4 = '\x05\x01\x00'
print(bytes(s4, encoding='ascii'))

# print('\n转变开始：')
# with Image(filename='img2.png') as pdf:
#     with pdf.convert('jpg') as image:
#         image.save(filename='result.jpg')

