import urllib
from HTMLParser import HTMLParser

def extract_source(url):
	urlsource = urllib.urlopen(url).read().decode('utf-8').encode('ascii', 'ignore')
	return urlsource

class TitleParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.titles = []
		self.titleflag = 0


	def handle_starttag(self, tag, attrs):
		self.titleflag = 0
		for name, values in attrs:
			if values == 'node-title':
				self.titleflag = 1



	def handle_data(self, data):
		if self.titleflag:
			self.titles.append(data)

titles_list = []

for i in range (1,6):

	thisamericanlife_source = extract_source \
	("http://www.thisamericanlife.org/radio-archives/episode/" + str(i) + "/")
	thisamericanlife_titles = TitleParser()
	thisamericanlife_titles.feed(thisamericanlife_source)
	titles_list.append(thisamericanlife_titles.titles[0])

print titles_list


