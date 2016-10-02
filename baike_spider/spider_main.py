# coding:utf-8
import url_manager, html_downloader, html_parser, html_outputer



class SpiderMain(object):
	def __init__(self):
		self.urls = url_manager.UrlManager()
		self.downloader = html_downloader.HtmlDownloader()
		self.parser = html_parser.HtmlParser()
		self.outputer = html_outputer.HtmlOutputer()

	def craw(self, root_url):
		self.urls.add_new_url(root_url)
		count = 1
		while self.urls.has_new_url():
			if count >100:
				break

			try:
				new_url = self.urls.get_new_url()
				count +=1
				html_content = self.downloader.download(new_url)

				new_urls, new_data = self.parser.parse(new_url, html_content)

				self.urls.add_new_urls(new_urls)

				self.outputer.collect_data(new_data)
			except:
				print('crawl failed!')

		self.outputer.output_html()




if __name__ == '__main__':
	root_url = "http://baike.baidu.com/view/21087.html"
	obj_spider = SpiderMain()
	obj_spider.craw(root_url)