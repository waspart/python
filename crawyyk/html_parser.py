from bs4 import BeautifulSoup
import re
import urllib.parse


class HtmlParser:
    def _get_new_urls(self, url, soup):
        new_urls = set()
        links = soup.find_all('a', href=re.compile(r'/nn/(.+)'))
        for link in links[:-3]:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(url, new_url)  # 值得研究
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_cont(self, url, soup):
        res_data = []
        trs = soup.find_all('tr')
        # print(len(trs))
        try:
            for tr in trs[1:]:
                tds = tr.find_all('td')
                # print(tds[5])
                ipaddr = tds[1].text.encode('utf-8')
                port = tds[2].text.encode('utf-8')
                httptype = tds[5].text.encode('utf-8')
                res_data.append(str(httptype, encoding='utf-8') + '*' + str(ipaddr, encoding='utf-8') + ':' + str(port, encoding='utf-8'))
        except:
            print('下标出错！！！')

        return res_data

    def parse(self, url, html_cont):
        if url is None or html_cont is None:
            return

        # soup = BeautifulSoup(html_cont, "html.parser", from_encoding="utf-8")

        soup = BeautifulSoup(html_cont, 'html.parser')
        new_urls = self._get_new_urls(url, soup)
        new_data = self._get_new_cont(url, soup)

        return new_urls, new_data
