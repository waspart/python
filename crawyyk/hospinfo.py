import pymysql
import requests
from bs4 import BeautifulSoup
import time

host = 'localhost'
port = 3306
username = 'root'
password = 'root'
db = 'cola'
charset = 'utf8'

conn = pymysql.connect(host=host,
                       port=port,
                       user=username,
                       password=password,
                       db=db,
                       charset=charset,
                       cursorclass=pymysql.cursors.DictCursor)
cursor = conn.cursor()

count_sql = 'select * from hosplinks'
limit_select_sql = 'select id, link, hospname, ifcrawed from hosplinks limit %s, %s'
update_sql = 'update hosplinks set ifcrawed = 1 where id = %s'
insert_sql = 'insert into hospinfos(hospname, hospksmc, hospxz, telephone, address, hospnickname,' +\
             'hospdist, hospyzname, hospconyear, hosptype, hospclass, hospkscount, hospyihucount, ' +\
             'hospbccount, hospmzcount, hospifyb, xjsbinfo, hospintro, hosphonor, website, busroutes)' +\
             ' values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'

# cursor.execute(count_sql)
# cursor.fetchall()
# totalcount = cursor.rowcount
totalcount = 47539
nolst = list(range(0, totalcount, 100))
nolst.append(totalcount)

header={
    'user-agent': 'Mozzila/5.0'
}

# cursor.execute(limit_select_sql % (0, 100))
# for link in cursor.fetchall():
#     print(link)

for no in nolst:
    if totalcount - no < 100:
        n = totalcount - no
    else:
        n = 100

    cursor.execute(limit_select_sql % (no, n))
    for linkinfo in cursor.fetchall():
        print('processing......', end='   ')
        update_flag = True
        id = linkinfo['id']
        hospname = linkinfo['hospname']
        ifcrawed = linkinfo['ifcrawed']
        link = linkinfo['link']
        if id == 1:
            continue
        # 如果该链接已经爬取过，则跳过该链接
        if ifcrawed == 1:
            continue
            update_flag = False

        insert_data = []

        # 第一个追加医院名称
        # print(linkinfo)
        # print(hospname)
        insert_data.append(hospname)

        # 医院主页面 内容获取
        html_req = requests.get(link, timeout=20, headers=header)
        html_cont = html_req.text
        soup = BeautifulSoup(html_cont, 'html.parser')

        # 获取当前医院的科室信息，并保存
        ksinfos = ''
        kscount = 1
        ks_cont = soup.find('div', class_='hp_docks')
        if ks_cont is not None:
            for ks in ks_cont.find_all('li'):
                ksmc = ks.find('a').text.strip()
                if kscount == 1:
                    ksinfos += ksmc
                else:
                    ksinfos += ',' + ksmc
                kscount += 1
        # 第二个追加科室信息
        insert_data.append(ksinfos)

        # 医院简介页面内容获取
        url = link + 'jianjie.html'
        url_req = requests.get(url, timeout=20, headers=header)
        url_cont = url_req.text
        # 如果下载失败，那么跳过该链接
        if html_req.status_code != 200 or url_req.status_code != 200:
            continue
            update_flag = False
        soup = BeautifulSoup(url_cont, 'html.parser')

        # 医院基本信息
        hospinfo = soup.find('div', class_='hpi_content')
        lis = hospinfo.find_all('li')
        yyxvinfo = lis[1].text.strip().split('：')[1]
        # print('\n医院性质：', yyxvinfo)
        # 第三个追加医院性质
        insert_data.append(yyxvinfo)

        yytelephont = lis[3].find('span').text.strip()
        # print('\n医院电话：', yytelephont)
        # 第四个追加医院电话
        insert_data.append(yytelephont)

        yyaddress = lis[4].find('span').text.strip()
        # print('\n联系地址：', yyaddress)
        # 第五个追加联系地址
        insert_data.append(yyaddress)

        hospbasicinfo = soup.find('div', class_='leftpad10 hpbasicinfo')
        bftds = hospbasicinfo.find_all('td')

        # 医院别名
        hospnickname = bftds[1].text.strip()
        # print('\n医院别名：', hospnickname)
        # 第六个追加医院别名
        insert_data.append(hospnickname)

        # 所属地区
        hospdist = bftds[3].text.strip()
        # print('\n所属区县：', hospdist)
        # 第七个追加所属区县
        insert_data.append(hospdist)

        # 院长姓名
        hospyvname = bftds[5].text.strip()
        # print('\n院长姓名：', hospyvname)
        # 第八个追加医院院长姓名
        insert_data.append(hospyvname)

        # 建院年份
        hospconyear = bftds[7].text.strip()
        # print('\n建院年份：', hospconyear)
        # 第九个追加建院年份
        insert_data.append(hospconyear)

        # 医院类型
        hosptype = bftds[9].text.strip()
        # print('\n医院类型：', hosptype)
        # 第十个追加医院类型
        insert_data.append(hosptype)

        # 医院等级
        hospclass = bftds[11].text.strip()
        # print('\n医院等级：', hospclass)
        # 第十一个追加医院等级
        insert_data.append(hospclass)

        # 科室数量
        hospkeuicount = bftds[13].text.strip()
        # print('\n科室数量：', hospkeuicount)
        # 第十二个追加科室数量
        insert_data.append(hospkeuicount)

        # 医护人数
        hospyihucount = bftds[15].text.strip()
        # print('\n医护人数：', hospyihucount)
        # 第十三个追加医护人数
        insert_data.append(hospyihucount)

        # 病床数量
        hospbkilcount = bftds[17].text.strip()
        # print('\n病床数量：', hospbkilcount)
        # 第十四个追加病床数量
        insert_data.append(hospbkilcount)

        # 年门诊量
        hospmfvfhucount = bftds[19].text.strip()
        # print('\n年门诊量：', hospmfvfhucount)
        # 第十五个追加年门诊量
        insert_data.append(hospmfvfhucount)

        # 是否医保
        hospifyibc = bftds[21].text.strip()
        # print('\n是否医保：', hospifyibc)
        # 第十六个追加是否医保
        insert_data.append(hospifyibc)

        # 先进设备信息，医院简介，荣誉 （这里可能缺失某一两项内容，需要特殊处理）
        someinfoconts = soup.find_all('div', class_='hpcontent')
        someinfotitles = soup.find_all('div', class_='hptitle')

        xjubinfo = ''
        yyjjinfo = ''
        honorinfo = ''

        for i in list(range(len(someinfotitles))):
            stitle = someinfotitles[i].text.strip()
            if stitle[-4:] == '设备信息':
                xjubinfo = someinfoconts[i - 1].text.strip()
            if stitle[-4:] == '医院简介':
                yyjjinfo = someinfoconts[i - 1].text.strip()
            if stitle[-4:] == '所获荣誉':
                honorinfo = someinfoconts[i - 1].text.strip()

        # 第十七个追加先进设备信息
        insert_data.append(xjubinfo)
        # 第十八个追加医院简介
        insert_data.append(yyjjinfo)
        # 第十九个追加医院荣誉
        insert_data.append(honorinfo)

        # # print(len(someinfos))
        # # print('someinfos:\n', someinfos)
        # xjubinfo = someinfos[0].text.strip()
        # # print('\n先进设备信息：', xjubinfo)
        # # 第十七个追加先进设备信息
        # insert_data.append(xjubinfo)
        #
        # yyjjinfo = someinfos[1].text.strip()
        # # print('\n医院简介：', yyjjinfo)
        # # 第十八个追加先进设备信息
        # insert_data.append(yyjjinfo)
        #
        # honorinfo = someinfos[2].text.strip()
        # # print('\n医院荣誉：', honorinfo)
        # # 第十九个追加先进设备信息
        # insert_data.append(honorinfo)

        # 联系信息
        contactinfos = soup.find('div', class_='leftpad10 contact').find_all('td')
        website = contactinfos[1].text.strip()
        # print('\n医院网址：', website)
        # 第二十个追加先进设备信息
        insert_data.append(website)

        busrounte = contactinfos[-1].text.strip()
        # print('\n公交线路：', busrounte)
        # 第二十一个追加先进设备信息
        insert_data.append(busrounte)

        cursor.execute(insert_sql, insert_data)
        print('插入第' + repr(cursor.lastrowid) + '条医院信息, Done!!!!!!!!')
        conn.commit()

        if update_flag:
            cursor.execute(update_sql % id)
            conn.commit()

        time.sleep(3)



