
from __future__ import with_statement

# importing contextlib module as it contains ContextManager class 
import contextlib

try:
	from urllib.parse import urlencode		# For parsing the URLs
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen		# For opening and closing URLs
except ImportError:							# Convert a mapping object to a percent-encoded ASCII text string
	from urllib2 import urlopen
import sys

def make_tiny(url):							# Converting the given url to short url
	request_url = ('http://tinyurl.com/api-create.php?' + 
	urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')

def main():
	s=input("\nEnter the url to convert: ")		# Input the url to be converted
	l=[]
	l.append(s)
	for tinyurl in map(make_tiny, l[0:]):			# Prints the converted url
		print("\nShort url is : ",tinyurl,"\n")

if __name__ == '__main__':
	main()