import TencentYoutuyun
import os

count = 0

# url = 'https://api.youtu.qq.com/youtu/ocrapi/generalocr'
appid = '10125301'
secretID = 'AKID89zmOpEC9uTr39MnJguwGPRIxTq1inQr'
secretKey = 'OeiaGAtRnxyrdDdszueWEBmJfsvnV1LT'
userid = '981466423'
end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT
# 生成鉴权码
youtu = TencentYoutuyun.YouTu(appid, secretID, secretKey, userid, end_point)
# 调用接口
# ret = youtu.generalocr(r'D:\python\PDF2TXT\file\images\img-1.png', data_type = 0)
_path = 'images/'
# 循环处理所有提取出的图片
imgs_lst = os.listdir(_path)
print('共有：', len(imgs_lst), '张图片')
for i in list(range(6451, 7160, 2)):
    img = 'page-' + repr(i) + '.png'
    if os.path.isfile(_path + img):
        print(repr(count), 'processing ' + img, end="  ")
        ret = youtu.generalocr('images/' + img, data_type=0)
        # print(ret)
        # with open('file\\ret' + repr(i) + '.txt', 'a+') as fin:
        #     fin.write(str(ret).encode('utf-8').decode('utf-8'))
        if 'items' in ret.keys():
            resstr_lst = ret['items']
        else:
            print('undo!!!!!')
            continue
        # print(len(resstr_lst))
        for i in list(range(len(resstr_lst))):
            # print(resstr_lst[i]['itemstring'].encode('iso-8859-1').decode('utf-8'), end="  ")
            f = open('mk2.txt', 'a+')
            f.write(resstr_lst[i]['itemstring'].encode('iso-8859-1').decode('utf-8'))
        # with open('mk2.txt', 'a+') as f:
        # 	print(resstr_lst[i]['itemstring'].encode('iso-8859-1').decode('utf-8'), end="  ")
        # 	f.write(resstr_lst[i]['itemstring'].encode('iso-8859-1').decode('utf-8'))
        count += 1
        print("Done!!!!!")

    if count % 100 == 0 and count != 0:
        print('############################')
        print('已处理：', repr(count), ' / 共有：', repr(len(imgs_lst)))
        print('############################')

print('All of the pages are processed!!!!!!!!')
