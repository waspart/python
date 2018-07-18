import html_downloader, html_parser
import sqlproc
import time

if __name__ == '__main__':
    print("############ 开始……")

    host = '115.159.193.122'
    port = 3306
    username = 'root'
    password = 'hkxx@206'
    db = 'cola'
    charset = 'utf8'
    sp = sqlproc.SqlProc(host, port, username, password, db, charset)
    downloader = html_downloader.HtmlDownloader()
    parser = html_parser.HtmlParser()

    select_sql = "select id, ifcrawed, link from linkstat limit %s, %s"
    update_sql = "update linkstat set ifcrawed = 1 where id = %s"
    insert_sql = "insert into jkkp(title, createdate, artcont) values(%s, %s, %s)"

    n = 100
    totalcount = 5760
    no_lst = list(range(0, totalcount, 100))
    no_lst.append(totalcount)

    for no in no_lst:
        if totalcount - no < 100:
            n = totalcount - no

        lst_link = sp.selectData(select_sql, (no, n))
        if lst_link == -1:
            '''查询失败，直接跳过'''
            continue

        for link in lst_link:
            print('crawing...... {}'.format(link), end="  ")
            uid = link['id']
            url = link['link']
            ifcrawed = link['ifcrawed']

            if ifcrawed == 1:
                '''该链接已经爬取过，直接跳过'''
                continue

            html_cont = downloader.download(url)
            if html_cont is None:
                '''获取内容为空， 直接跳过'''
                continue

            parse_result = parser.parse(html_cont)
            if parse_result is not None:
                print(parse_result, end="  ")
                bs, code = sp.insertData(insert_sql, parse_result)
                if bs:
                    print('插入成功！ 第 {} 条记录。'.format(code), end="  ")
                    if sp.updateData(update_sql, uid):
                        print('更新成功， Done!')
                    else:
                        print('更新失败， Undo!')
                else:
                    print('插入失败！')
            else:
                print('爬取失败！')
            time.sleep(1)
