import html
from bs4 import BeautifulSoup as bs
import urllib.parse
import requests
from pprint import pprint

class Torrent:
	def __init__(self, q, limit=15):
		""" piratebay search engine
			q         : query for search
			limit     : maximum result count
		"""
		self.q = urllib.parse.quote(q)
		self.max = limit
		self._rawhtml = ''
		self._torrents = []
		self._magnets = []
		self._rows = []
		self._links_with_data = []

		self.run_crawl()

	def run_crawl(self):
		url = f'https://tpb.party/search/{self.q}'
		try:
			req = requests.get(url=url)
		except:
			pprint('[Error] - Try again after a few seconds!')
		else:
			soup = bs(req.text, 'html.parser')
			# print(soup)
			self._torrents = soup.find_all('tr')[1:-1]

	@property
	def raw(self):
		return self._rawhtml

	@property
	def links_with_data(self):
		findtitle = lambda x: x.find('a', {'class': 'detLink'}).text
		findmagnet =  lambda x: x.find('a', {'title': 'Download this torrent using magnet'})['href']
		finddateuploader = lambda x: x.find('font', {'class': 'detDesc'}).text
		seedandleech = lambda x: list(map(lambda x: x.text, 
		x.find_all('td', {'align': 'right'})))
		findlink = lambda x: x.find('a', {'class': 'detLink'})['href']

		for count,torrent in enumerate(self._torrents):
			if count == self.max:
				break

			title = findtitle(torrent)
			magnet = findmagnet(torrent)
			link = findlink(torrent)
			dateuploader = finddateuploader(torrent)
			seedleechcount = seedandleech(torrent)
		
			self._links_with_data.append({
				'title': html.unescape(title),
				'dateuploader': html.unescape(dateuploader),
				'magnet': magnet,
				'link': link,
				'seeders': seedleechcount[0],
				'leechers': seedleechcount[1]
				})

		return self._links_with_data

	
if __name__ == "__main__":
	Data = Torrent("avengers")
	pprint(Data.raw)
	pprint(Data.links_with_data)
