# coding:utf-8
import urllib.request


class HtmlDownloader(object):
	def download(self, url):

		print('begin urlopen, ', url)
		response = urllib.request.urlopen(url)
		print('after urlopen')
		code = response.getcode()
		print('code=', code)
		if code != 200:
			return None
		return response.read()
