import requests
from bs4 import BeautifulSoup
import time
import random
import sqlproc

root_url = r'http://www.360changshi.com/'
# sqlsp = sqlproc.SqlProc()

host = 'localhost'
port = 3306
username = 'root'
password = 'root'
db = 'cola'
charset = 'utf8'
sqlsp = sqlproc.SqlProc(host, port, username, password, db, charset)
insert_sql = 'insert into urlstat(link, ifcrawed) values(%s, %s)'

def parse(html_cont):
    level2_urls = set()
    new_urls = set()
    soup_2 = BeautifulSoup(html_cont, 'html.parser')

    # 目标链接
    lists = soup_2.find_all('div', class_='list')
    for l in lists:
        new_urls.add(l.find('h3').find('a')['href'])
    
    # 2级链接
    paging = soup_2.find('div', class_='paging')
    spans = paging.find_all('span')
    for sp in spans:
        if sp.find('a') is not None:
            level2_urls.add(root_url + sp.find('a')['href'])

    return new_urls, level2_urls

head={
    'user-agent': 'Mozila/5.0'
}
res = requests.get(root_url, headers=head, timeout=60)

if res.status_code == 200:
    soup = BeautifulSoup(res.text, 'html.parser')
    uls = soup.find('div', class_='leveltwo-list-content').find_all('ul')
    for ul in uls[:-1]:
        lis = ul.find_all('li')

        for li in lis:
            url = li.find('a')['href']
            # print()
            # print('########################')
            # print('#####开始')
            # print('########################')
            # print('标题：{}, 链接：{}, 页数： '.format(li.find('a')
            #     .text.encode('iso-8859-1').decode('utf-8'), url), end="  ")
            # print(url)

            set_level2_urls = set()
            set_level2_urls_done = set()
            set_new_urls = set()
            set_level2_urls.add(url)

            while len(set_level2_urls) >= 1:
                this_url = set_level2_urls.pop()
                res_2 = requests.get(this_url, headers=head, timeout=60)
                set_level2_urls_done.add(this_url)
                if res_2.status_code == 200:
                    new_urls, level2_urls = parse(res_2.text)
                    for uri in new_urls:
                        set_new_urls.add(uri)
                        bs, code = sqlsp.insertData(insert_sql, (uri, 0))
                        if bs:
                            print('插入成功！第 {} 条数据'.format(code), end="  ")
                        else:
                            print('插入失败！')
                        print('Done!')

                    for uri in level2_urls:
                        if uri not in set_level2_urls_done:
                            set_level2_urls.add(uri)
                    # soup_2 = BeautifulSoup(res_2.text, 'html.parser')
                    # total_page_no = 1
                    # paging = soup_2.find('div', class_='paging')
                    # spans = paging.find_all('span')
                    # if len(spans) > 1:
                    #     # spans = paging.find_all('span')
                    #     # total_page_no = int(spans[-2].text)
                    # print(total_page_no)

                    # # for i in list(range(total_page_no)):
                else:
                    print('跳过')
                    continue
                time.sleep(random.random())
            print()
            print('##################################')
            print('标题：{}, 链接：{}, 页数： {}'.format(li.find('a').text.encode('iso-8859-1').decode('utf-8'), url, len(set_new_urls)))
            print('##################################')

            # print(len(set_new_urls))

            # if len(set_new_urls) // 15 + 1 == len(set_level2_urls_done):
            #     print('正常')
            # else:
            #     print('不正常')

            # print('########################')
            # print('#####结束')
            # print('########################')
                    

            time.sleep(random.random())

