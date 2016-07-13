import urllib
from HTMLParser import HTMLParser

#Open source as string
def extract_source(url):
	url_source = urllib.urlopen(url).read().decode('utf-8').encode('ascii', 'ignore')
	return url_source