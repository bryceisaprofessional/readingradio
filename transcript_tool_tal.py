#Transcript tool to pull book references out of This American Life broadcasts.

import urllib
from HTMLParser import HTMLParser

#Open source as string
def extract_source(url):
	url_source = urllib.urlopen(url).read().decode('utf-8').encode('ascii', 'ignore')
	return url_source

#HTMLParser to grab data and strip tags
class DataParser(HTMLParser):

	def __init__(self):
		HTMLParser.__init__(self)
		self.data_list = []
		self.content_flag = 0

	def handle_starttag(self, tag, attrs):
		for name, value in attrs:
			if value == 'radio-wrapper':
				self.content_flag = 1
	
	def handle_data(self, data):
		if self.content_flag:
			self.data_list.append(data)


#specific search for books, author
def book_search(array):
	context_range = 30
	index_count =  0
	found_array = []
	context_array = []

	for i in array:
		index_count += 1
		context_list = []
		if ('book' in i.lower() or 'author' in i.lower()) \
		and ('facebook' not in i.lower()):
			
			found_array.append("<|"+str(i).upper()+"|>" + " found at: "+ str(index_count))
			
			for j in range(index_count - context_range/2, index_count + context_range):
				
				if j == index_count - 1: 
					context_list.append("<|" + array[j].upper() + "|>")
				else:
					context_list.append(array[j])
			
			context_array.append(' '.join(context_list))

	return context_array

#Setup, may be looped to extract multiple references from multiple links


for i in range(1,10):
	thisamericanlife_source = extract_source\
("http://www.thisamericanlife.org/radio-archives/episode/"+ str(i) +"/transcript")

	thisamericanlife_data = DataParser()
	thisamericanlife_data.feed(thisamericanlife_source)

	transcript_list = "".join(thisamericanlife_data.data_list).split(' ')

	print "EPISODE: " + str(i)
	print "=" * 80
	for i in book_search(transcript_list):
		print i + "\n"
