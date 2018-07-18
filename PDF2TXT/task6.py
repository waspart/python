# 提取pdf中的图片 failed

from PyPDF2 import PdfFileReader, PdfFileWriter
from wand.image import Image
from wand.drawing import Drawing
from wand.color import Color


def resize_photo(filename, width, height, target):
    with Image(filename=filename) as img:
        img.resize(width, height)
        img.save(filename=target)


memo = {}

def getPdfReader(filename):
    reader = memo.get(filename, None)
    if reader is None:
        reader = PdfFileReader(filename, strict=Flase)
        memo[filename] = reader
        return reader


pdf_im = PdfFileReader(open(r'D:\python\PDF2TXT\file\tnb.pdf', 'rb'))
npage = pdf_im.getNumPages()
# print(npage)
# print(isinstance(npage, int))

page = pdf_im.getPage(1)
# print(page)

# resize_photo('1.jpg', 100, 100, '2.jpg')

image_pdf = Image(filename=r'D:\python\PDF2TXT\nkx.pdf')
image_jpeg = image_pdf.convert('bmp')

req_image = []
for img in image_jpeg.sequence:
    image_page = Image(image=img)
    req_image.append(image_page.make_blob('png'))

i = 0
for img in req_image:
    ff = open(r'D:\python\PDF2TXT\images\imagesfile_out-' + str(i) + '.bmp', 'wb')
    ff.write(img)
    ff.close()
    i += 1
