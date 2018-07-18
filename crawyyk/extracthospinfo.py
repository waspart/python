import requests
from bs4 import BeautifulSoup


# url = r'http://yyk.99.com.cn/luyang/77807/jianjie.html'
url = r'http://yyk.99.com.cn/huangpu/68677/jianjie.html'

header = {
    'user-agent': 'my-app/0.0.1'
}
res = requests.get(url, headers=header, timeout=20)
html = res.text

soup = BeautifulSoup(html, 'html.parser')

# 医院名称
# hospname = soup.find('div', class_='hospital_name').text.strip()
hospname = soup.find('h1').text.strip()
print('\n医院名称：', hospname)

hospinfo = soup.find('div', class_='hpi_content')
lis = hospinfo.find_all('li')
yyxvinfo = lis[1].text.strip().split('：')[1]
print('\n医院性质：', yyxvinfo)
yytelephont = lis[3].find('span').text.strip()
print('\n医院电话：', yytelephont)
yyaddress = lis[4].find('span').text.strip()
print('\n联系地址：', yyaddress)

# 医院基本信息
hospbasicinfo = soup.find('div', class_='leftpad10 hpbasicinfo')
bftds = hospbasicinfo.find_all('td')

# 医院别名
hospnickname = bftds[1].text.strip()
print('\n医院别名：', hospnickname)

# 所属地区
hospdist = bftds[3].text.strip()
print('\n所属区县：', hospdist)

# 院长姓名
hospyvname = bftds[5].text.strip()
print('\n院长姓名：', hospyvname)

# 建院年份
hospconyear = bftds[7].text.strip()
print('\n建院年份：', hospconyear)

# 医院类型
hosptype = bftds[9].text.strip()
print('\n医院类型：', hosptype)

# 医院等级
hospclass = bftds[11].text.strip()
print('\n医院等级：', hospclass)

# 科室数量
hospkeuicount = bftds[13].text.strip()
print('\n科室数量：', hospkeuicount)

# 医护人数
hospyihucount = bftds[15].text.strip()
print('\n医护人数：', hospyihucount)

# 病床数量
hospbkilcount = bftds[17].text.strip()
print('\n病床数量：', hospbkilcount)

# 年门诊量
hospmfvfhucount = bftds[19].text.strip()
print('\n年门诊量：', hospmfvfhucount)

# 是否医保
hospifyibc = bftds[21].text.strip()
print('\n是否医保：', hospifyibc)


# 先进设备信息，医院简介，荣誉
someinfoconts = soup.find_all('div', class_='hpcontent')
someinfotitles = soup.find_all('div', class_='hptitle')
# print(len(someinfoconts))
# print(len(someinfotitles))
# print(someinfoconts)


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

print('设备信息：', xjubinfo)
print('医院简介：', yyjjinfo)
print('所获荣誉：', honorinfo)


# print(len(someinfos))
# print('someinfos:\n', someinfos)
# xjubinfo = someinfos[0].text.strip()
# print('\n先进设备信息：', xjubinfo)
# yyjjinfo = someinfos[1].text.strip()
# print('\n医院简介：', yyjjinfo)
# honorinfo = someinfos[2].text.strip()
# print('\n医院荣誉：', honorinfo)

contactinfos = soup.find('div', class_='leftpad10 contact').find_all('td')

website = contactinfos[1].text.strip()
print('\n医院网址：', website)
# telephone = contactinfos[3].text.strip()
# print('\n医院电话：', telephone)
# address = contactinfos[5].text.strip()
# print('\n医院地址：', address)
# postcode = contactinfos[7].text.strip()
# print('\n医院邮编：', postcode)
busrounte = contactinfos[-1].text.strip()
print('\n公交线路：', busrounte)




