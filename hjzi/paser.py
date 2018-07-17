from bs4 import BeautifulSoup


class Parser(object):

    def parseDiv(self, html_cont):
        if html_cont is None or html_cont.strip() == "":
            return None

        soup = BeautifulSoup(html_cont, 'lxml')
        lst_box = soup.find_all("div", class_="groupbox clearfix")
        results = set()
        for box in lst_box:
            head = box.find("div", class_="groupbox_head")
            py = head.find("span").text
            lst_a = box.find_all("a")
            for item in lst_a:
                results.add(item['href'] + "#" + py + "#" + item.text[-1])

        return results

    def parseDict(self, html_cont):
        if html_cont is None or html_cont.strip() == "":
            return None

        soup = BeautifulSoup(html_cont, 'lxml')

        # 查找类别
        kind = soup.find("div", class_="introduce").find("span", class_="spwid120").text.strip()  

        # 查找笔顺
        lst_label = soup.find("div", id="sub_con").find_all(
            "div", class_="label")
        for label_item in lst_label:
            if "笔顺" in label_item.find("div").text:
                biuy = label_item.find("span").text

        # 基本释义
        lst_basic_p = soup.find(
            "div", class_="view_con con_basic clearfix").find_all("p")
        con_basic = ""
        for item_basic_p in lst_basic_p:
            con_basic += item_basic_p.text + "\n"

        # 详细释义
        lst_xx_p = soup.find("div", class_="view_con clearfix").find_all("p")
        con_xx = ""
        for item_xx_p in lst_xx_p:
            con_xx += item_xx_p.text + "\n"

        return (kind, biuy, con_basic, con_xx)
