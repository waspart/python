import requests
import os
import time

head = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC1YYES/' # 一年级上册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC1YYEX/' # 一年级下册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC2YYDS/' # 二年级上册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC2YYDX/' # 二年级下册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC3YYES/' # 三年级上册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC3YYEX/' # 三年级下册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC4YYES/' # 四年级上册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC4YYEX/' # 四年级下册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC5YYES/' # 五年级上册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC5YYEX/' # 五年级下册链接
url_pre = 'http://auto.tom61.com/f/yshb/002/RJC6YYES/' # 六年级上册链接
# url_pre = 'http://auto.tom61.com/f/yshb/002/RJC6YYEX/' # 六年级下册链接

def getCont(url):
    req  = requests.get(url, headers=head)
    if req.status_code == 200:
        return req.content
    else:
        return -1


def write(file_path, file_content):
    try:
        with open(file_path, 'wb') as fin:
            fin.write(file_content)
        return True
    except:
        return False

if __name__ == '__main__':
    _path = 'liunianjishangce'
    if not os.path.isdir(_path):
        os.mkdir(_path)
    for i in list(range(120)):
        if i < 10:
            audio_url = url_pre + '00' + repr(i) + '.mp3'
            img_url = url_pre + '00' + repr(i) + '.jpg'
            audio_path = _path + os.sep + '00' + repr(i) + '.mp3'
            img_path = _path + os.sep + '00' + repr(i) + '.jpg'
        else:
            audio_url = url_pre + '0' + repr(i) + '.mp3'
            img_url = url_pre + '0' + repr(i) + '.jpg'
            audio_path = _path + os.sep + '0' + repr(i) + '.mp3'
            img_path = _path + os.sep + '0' + repr(i) + '.jpg'
        print("processing " + repr(i), end="  ")
        if getCont(img_url) != -1:
            print('保存该图片', end="  ")
            if write(img_path, getCont(img_url)):
                print('保存成功！', end="  ")
            else:
                print('保存失败！', end="  ")
        else:
            print('该图片不存在', end="  ")

        if getCont(audio_url) != -1:
            print('保存该音频', end="  ")
            if write(audio_path, getCont(audio_url)):
                print('保存成功！', end="  ")
            else:
                print('保存失败！', end="  ")
        else:
            print('该音频不存在', end="  ")
        print('完成！')
        time.sleep(1)
