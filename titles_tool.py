#short TAL site scrubber to pull titles from each episode
#output to csv file is probably best.

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

for i in range (465,591):

	tal_source = extract_source \
	("http://www.thisamericanlife.org/radio-archives/episode/" + str(i) + "/")
	tal_titles = TitleParser()
	tal_titles.feed(tal_source)
	print tal_titles.titles[0]
	titles_list.append(tal_titles.titles[0])

titles_file = open("TAL_titles.csv", 'a') 

for i in titles_list:
	titles_file.write(i + "\n")

print "wrote titles to TAL_titles.csv"


