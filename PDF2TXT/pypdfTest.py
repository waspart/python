from PyPDF2 import PdfFileReader, PdfFileWriter
# import PythonMagick
from wand.image import Image
from wand.color import Color
import io


_path = 'nkx.pdf'
pdfReader = PdfFileReader(_path)
docInfo = pdfReader.getDocumentInfo()
print('文档信息：', docInfo)

# pageMode = pdfReader.getPageMode()
# print('页面模式：', pageMode)

pageCount = pdfReader.getNumPages()
print('总页数：', pageCount)
for ind in list(range(2)):
    pageObj = pdfReader.getPage(ind)
    # print('index = %d, pageObj = %s' % (ind, type(pageObj)))
    pageNo = pdfReader.getPageNumber(pageObj)
    # print('当前页数：', pageNo)

    # img = PythonMagick.Image()
    # img.magic('png')
    # img.write('images/img-' + str(ind) + '.png')

    # dst_pdf = PdfFileWriter()
    # dst_pdf.addPage(page=pageObj)
    # pdf_bytes = io.BytesIO()
    # dst_pdf.write(pdf_bytes)
    # pdf_bytes.seek(0)
    # img = Image(file=pdf_bytes, resolution=120)
    # img.format = 'png'
    # img.compression_quality = 100
    # img.background_color = Color('white')
    # img_path = 'images/img-' + str(ind) + '.png'
    # img.save(filename=img_path)
    # img.destroy()

    print('提取文字结果：', pageObj.extractText())
    lst = pageObj.getContents()
    print(lst is None)
    print(type(lst))
    if isinstance(lst, list):
        print(len(lst))
    for ls in lst:
        print(type(ls))

    # dst_pdf = PdfFileWriter()
    # dst_pdf.addPage(pageObj)
    # pdf_stream = io.BytesIO()
    # dst_pdf.write(pdf_stream)
    # pdf_stream.seek(0)
    # print(type(pdf_stream))
    with Image(file=object(lst)) as img:
        print(img is None)
        print(len())
        with img.convert('png') as imgpng:
            imgpng.save('result.png')

print('\nDone!!!!!!!!!!')


