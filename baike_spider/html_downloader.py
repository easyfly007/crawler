# coding:utf-8
import urllib.request


class HtmlDownloader(object):
	def download(self, url):
		response = urllib.request.urlopen(url)
		code = response.getcode()
		if code != 200:
			return None
		return response.read()
