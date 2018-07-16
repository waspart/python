from bs4 import BeautifulSoup


class Parser(object):

    def parseDiv(self, html_cont):
        if html_cont is None or html_cont.strip() == "":
            return None

        soup = BeautifulSoup(html_cont, 'lxml')
        box = soup.find("div", class_="groupbox clearfix")

        head = box.find("div", class_="groupbox_head")
        py = head.find("span").text
        lst_a = box.find_all("a")
        results = set()
        for item in lst_a:
            results.add(item['href'] + "#" + py)

        return results
