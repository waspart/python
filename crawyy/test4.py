import requests
import os
import time

'''
人教版小学英语（三年级起步）电子教材爬取
'''

head = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}

url_pre = r'http://auto.tom61.com/f/yshb/002/'
lst_url = ['RJC3YYCS', 'RJC3YYCX', 'RJC4YYCS', 'RJC4YYCX', 'RJC5YYCS', 'RJC5YYCX', 'RJC6YYCS', 'RJC6YYCX']
lst_dir = ['sannianjishangce', 'sannianjixiace', 'sinianjishangce', 'sinianjixiace',
            'wunianjishangce', 'wunianjixiace', 'liunianjishangce', 'liunianjixiace']


def getCont(url):
    req  = requests.get(url, headers=head)
    if req.status_code == 200:
        return req.content
    else:
        return -1


def writeFile(file_path, file_content):
    try:
        with open(file_path, 'wb') as fin:
            fin.write(file_content)
        return True
    except:
        return False

if __name__ == '__main__':

    if len(lst_dir) != len(lst_url):
        print("数量有误")
        exit

    for i in list(range(len(lst_dir))):
        _path = lst_dir[i]
        if not os.path.isdir(_path):
            print("文件夹不存在！", end="    ")
            os.mkdir(_path)
            print("创建成功!!!")

        url = url_pre + lst_url[i] + '/'

        for i in list(range(120)):
            if i < 10:
                audio_url = url + '00' + repr(i) + '.mp3'
                img_url = url + '00' + repr(i) + '.jpg'
                audio_path = _path + os.sep + '00' + repr(i) + '.mp3'
                img_path = _path + os.sep + '00' + repr(i) + '.jpg'
            else:
                audio_url = url + '0' + repr(i) + '.mp3'
                img_url = url + '0' + repr(i) + '.jpg'
                audio_path = _path + os.sep + '0' + repr(i) + '.mp3'
                img_path = _path + os.sep + '0' + repr(i) + '.jpg'
            print("processing " + repr(i), end="  ")
            # print(audio_url, end="  ")
            if getCont(img_url) != -1:
                print('保存该图片', end="  ")
                if writeFile(img_path, getCont(img_url)):
                    print('保存成功！', end="  ")
                else:
                    print('保存失败！', end="  ")
            else:
                print('该图片不存在', end="  ")

            if getCont(audio_url) != -1:
                print('保存该音频', end="  ")
                if writeFile(audio_path, getCont(audio_url)):
                    print('保存成功！', end="  ")
                else:
                    print('保存失败！', end="  ")
            else:
                print('该音频不存在', end="  ")
            print('完成！')
            time.sleep(1)
