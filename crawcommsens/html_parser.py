from bs4 import BeautifulSoup

class HtmlParser(object):
    
    def parse(self, html_cont):
        result = []
        if html_cont is None:
            return None
        soup = BeautifulSoup(html_cont, 'html.parser')
        main_cont = soup.find('div', class_='article')
        if main_cont is None:
            return None

        title_text = ''
        try:
            title = main_cont.find('h1')
            if title is not None:
                title_text = title.text.encode('iso-8859-1').decode('utf-8')    
        except:
            print('解析标题出现编码异常', end="  ")
        finally:
            result.append(title_text)

        # createDate = main_cont.find('div', class_='bk_qwkp_xqin_l fl').find('span').text
        # result.append(createDate)

        summary_text = ''
        try:
            summary = main_cont.find('div', class_='summary').text
            if summary is not None:
                summary_text = summary.encode('iso-8859-1').decode('utf-8')
        except:
            print('解析导语出现编码异常', end="  ")
        finally:
            result.append(summary_text)

        artcont = ''
        try:
            cont = main_cont.find('div', class_='desc')
            if cont is not None:
                ps = cont.find_all('p')
                for con in ps:
                    conc = p.text.encode('iso-8859-1').decode('utf-8')
                    artcont += conc
                    # artcont += con.text.encode('iso-8859-1').decode('utf-8')
            # artcont = artcont.encode('iso-8859-1').decode('utf-8')

        except:
            print('解析文章内容出现编码异常', end="  ")
        finally:
            result.append(artcont)


        return result
        