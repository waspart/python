import downloader, outputer, htmlparser
import time
import random
import os

class SpiderMain(object):
	
	"""
	爬虫目的：
       爬取瑞文网https://www.ruiwen.com/
       电子版中小学教材

	"""

	def __init__(self):
		self.downloader = downloader.Downloader()
		self.parser = htmlparser.HtmlParser()
		self.outputer = outputer.Outputer()
		self.count = 86
		self.link_lst = []
		# print('init successfully!!!!!')

	def craw(self, url, img_dir):
		print("crawing.... ", url, end="  ")
		html_cont = self.downloader.download(url)
		if html_cont != -1:
			# 获取成功
			img_url, new_url = self.parser.parse(html_cont)
			img_cont = self.parser.getImg(img_url)

			img_name = 'page' + repr(self.count) + '.jpg'
			if self.outputer.saveImg(img_cont, img_dir + os.sep + img_name):
				print("Done!!!!!!!")
				self.count += 1
				self.link_lst.append(url)
			else:
				print("Failed!!!!!")
			
			if new_url in self.link_lst:
				print("该书抓取结束, 共有" + repr(self.count) + "张图片")					
				return 0
			else:
				# time.sleep(random.random())
				self.craw(new_url, img_dir)

		return 0

		
if __name__ == '__main__':
	
	# img_dir = "d:\\files\\books\\"
	# this_dir = ""
	# pre_url = "https://www.ruiwen.com"
	# root_url = ""  # 本次需要爬取的根路径

	# print("crawing.... ", root_url, end="  ")
	# fread = open('top_links.txt', 'r')
	# lst_ver = fread.read().split('#')
	# for ver in lst_ver:
	# 	lst_link = ver.split('*')
	# 	for i in list(range(len(lst_link))):
	# 		if i == 0:
	# 			this_dir = img_dir + lst_link[i]
	# 			# if not os.path.exists(this_dir):
	# 			# 	os.mkdir(this_dir)
	# 		else:
	# 			root_url = pre_url + lst_link[i]
	# 			ce = lst_link[i].split('/')[-2]
	# 			this_dir += os.sep + ce
	# 			# print(this_dir)
	# 			if not os.path.exists(this_dir):
	# 				os.makedirs(this_dir)

	# 			spider = SpiderMain()
	# 			spider.craw(root_url, this_dir)
	# 			this_dir = this_dir[:-(len(ce) + 1)]				

	# fread.close()


	# root_url = "http://www.ruiwen.com/jiaocai/yuwen/beishida/wunianjishangce/shangce1.html"
	# img_dir = r"D:\Files\books\北师大版\wunianjishangce\\"
	# spider = SpiderMain()
	# spider.craw(root_url, img_dir)

	# root_url = "http://www.ruiwen.com/jiaocai/yuwen/beishida/wunianjixiace/xiace1.html"
	# img_dir = r"D:\Files\books\北师大版\wunianjixiace\\"
	# spider = SpiderMain()
	# spider.craw(root_url, img_dir)

	# root_url = "http://www.ruiwen.com/jiaocai/yuwen/beishida/liunianjishangce/shangce1.html"
	# img_dir = r"D:\Files\books\北师大版\liunianjishangce\\"
	# spider = SpiderMain()
	# spider.craw(root_url, img_dir)

	root_url = "http://www.ruiwen.com/jiaocai/yuwen/beishida/liunianjixiace/xiace87.html"
	img_dir = r"D:\Files\books\北师大版\liunianjixiace\\"
	spider = SpiderMain()
	spider.craw(root_url, img_dir)
