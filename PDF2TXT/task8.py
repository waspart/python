# pdfminer 处理pdf文件

import importlib
import sys
import random
from urllib.request import urlopen, Request

from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed
from pdfminer.pdfparser import PDFParser, PDFDocument

importlib.reload(sys)


def parse_pdf(_path):
    fp = open(_path, 'rb')
    parser = PDFParser(fp)

    # 创建一个pdf文档
    doc = PDFDocument()
    # 连接分析器与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)
    # 提供初始密码，如果没有密码，提供空
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF资源管理器 管理共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        lap = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=lap)
        # 创建一个PDF解释器对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历pdf页面列表，分页处理
        for page in doc.get_pages():
            # 解释器处理当前页面内容
            interpreter.process_page(page)
            # 接受当前页面LTPage对象
            ltps = device.get_result()
            # LTPage对象ltps中存放着当前页面解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等 想要获取文本就获得对象的text属性
            for ltp in ltps:
                if isinstance(ltp, LTTextBoxHorizontal):
                    results = ltp.get_text()
                    print('results: ' + results)


if __name__ == '__main__':
    _path = r'D:\python\PDF2TXT\nkx.pdf'
    parse_pdf(_path)
