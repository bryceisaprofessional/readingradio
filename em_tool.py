import urllib
from HTMLParser import HTMLParser

#Open source as string
def extract_source(url):
	url_source = urllib.urlopen(url).read().decode('utf-8').encode('ascii', 'ignore')
	return url_source

#HTMLParser to grab data and strip tags
class ItalicsParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.italic_tag = 0
		self.title_data = []

	def handle_starttag(self, tag, attrs):
		if tag == 'i':
			self.italic_tag = 1
	
	def handle_data(self, data):
		if self.italic_tag and ('this' not in data.lower() and \
			'american' not in data.lower() and\
			'life' not in data.lower() ):
			self.title_data.append(data)
		self.italic_tag = 0


for i in range(201,211):

	tal_source = extract_source \
		("http://www.thisamericanlife.org/radio-archives/episode/" + str(i) + "/transcript")
	tal_titles = ItalicsParser()
	tal_titles.feed(tal_source)
	print "EPISODE: " + str(i)
	print "=" * 80 + "\n"
	print ' '.join(tal_titles.title_data) + "\n"

