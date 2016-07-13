#script to grab emphasis tags in transcripts, these contain the titles of books
#and publications referenced. 

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

media_titles = open('em_titles.txt','a')

for i in range(211,301):

	tal_source = extract_source \
		("http://www.thisamericanlife.org/radio-archives/episode/" + str(i) +\
		 "/transcript")
	tal_titles = ItalicsParser()
	tal_titles.feed(tal_source)
	media_titles.write("EPISODE: " + str(i)+ "\n")
	media_titles.write("=" * 80 + "\n")
	media_titles.write(' '.join(tal_titles.title_data) + "\n" + "\n")


print "finished writing titles"