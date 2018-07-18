import requests
import time
from bs4 import BeautifulSoup


waittime = 90
root_url = "https://www.merriam-webster.com"
url = "https://www.merriam-webster.com/browse/dictionary/a"
headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

res_1 = requests.get(url, headers=headers, timeout=90).text
soup_1 = BeautifulSoup(res_1, "html.parser")
lst_1 = soup_1.find("div", class_="alphalinks").find_all("li")
# print(lst_1)
lst_link = []
for item in lst_1:
    lst_link.append(item.find("a")["href"])
print(len(lst_link))

for link in lst_link:
    print(link + "    begins. \t", end="  ")
    
    this_url = root_url + link
    try:
        res_2 = requests.get(this_url, headers=headers, timeout=90).text
    except:
        print(this_url + "出现异常")
        continue

    soup_2 = BeautifulSoup(res_2, "html.parser")
    pageinfo = soup_2.find("div", class_="archives").find("span", class_="counters").text
    page_count = int(pageinfo.split(" ")[-1])
    print("页数：" + repr(page_count), end="  ")

    # for ind in list(range(1, page_count + 1)):
        
    #     url_3 = this_url + "/" + str(ind)
    #     try:
    #         res_3 = requests.get(url_3, headers=headers, timeout=90).text
    #     except:
    #         print(url_3 + "出现异常")
    #         continue

    #     soup_3 = BeautifulSoup(res_3, "html.parser")
    #     entries = soup_3.find("div", class_="entries").find_all("a")

    #     for entry in entries:
    #         word = entry.text
    #         with open("words.txt", "a+", encoding="utf-8") as fw:
    #             fw.write(word + "\n")

    time.sleep(1)

    print("Done!!!!!!!")




