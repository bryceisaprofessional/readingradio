import urllib
from HTMLParser import HTMLParser

def extract_source(url):
	url_source = urllib.urlopen(url).read().decode('utf-8').encode('ascii', 'ignore')
	return url_source

class DataParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.data_list = []

	def handle_data(self, data):
		self.data_list.append(data)

thisamericanlife_source = extract_source\
("http://www.thisamericanlife.org/radio-archives/episode/362/transcript")

thisamericanlife_data = DataParser()
thisamericanlife_data.feed(thisamericanlife_source)

transcript_list = "".join(thisamericanlife_data.data_list).split(' ')

for i in  transcript_list:
	if i.lower() == 'book' or i.lower() == 'author':
		print i
