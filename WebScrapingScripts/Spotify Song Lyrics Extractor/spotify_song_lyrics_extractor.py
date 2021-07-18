import json
import re
import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials #To access contents of spotify desktop website
from bs4 import BeautifulSoup #Used for scraping web page

'''Credentials initially set to None
   Later on we access these spotify credentials through API_Credentials.json file'''
spotify_client_id = None 
spotify_client_secret = None
genius_client_secret = None

'''Class to scrape lyrics by calling google_lyrics function and store values like
   title, artist, lyrics, source, query for each song'''
class GetLyrics:
	def __init__(self):
		self.title = None
		self.artist = None
		self.lyrics = None
		self.source = None
		self.query = None

	def google_lyrics(self, query):
		'''This function will scrape lyrics of a particular song from the google along
		   with its title,author and source of the song and display
		   it in console'''
		query = str(query)
		try:
			url = "https://www.google.com/search?q=" + query.replace(" ", "+") + "+lyrics"
			print(url)

			r = requests.get(url)
			htmlcontent = r.content
			html_content = BeautifulSoup(htmlcontent, "lxml")

			title = str(html_content.find("span", class_="BNeawe tAd8D AP7Wnd"))
			title = re.sub(r"(<.*?>)*", "", title).replace("[", "").replace("]", "")
			print("Title:",title)

			artist = html_content.find_all("span", class_="BNeawe s3v9rd AP7Wnd")
			artist = str(artist[1])
			artist = re.sub(r"(<.*?>)*", "", artist).replace("[", "").replace("]", "")
			print("Artist:",artist)

			lyrics = html_content.find_all("div", class_="BNeawe tAd8D AP7Wnd")
			lyrics = str(lyrics[2])
			lyrics = re.sub(r"(<.*?>)*", "", lyrics).replace("[", "").replace("]", "")

			source = str(html_content.find("span", class_="uEec3 AP7Wnd"))
			source = re.sub(r"(<.*?>)*", "", source).replace("[", "").replace("]", "")

			if lyrics is None or artist is None or title is None or source is None:
				raise Exception("Something went wrong. No lyrics yielded. ")

			self.title = title 
			self.artist = artist 
			self.lyrics = lyrics  
			self.source = source  
			self.query = query
		except:
			raise Exception


def get_lyrics(full_title):
	'''This function will call class and its function to get lyrics'''
	query_title = str(full_title)  
	query_title = re.sub(r'[^\w]', ' ', query_title) #Removes every character except alphabets and digits
	query_title = re.sub(' +', ' ', query_title) #Removes extra spaces between words

	ly = GetLyrics()
	try:
		ly.google_lyrics(query_title)
	except:
		print("Not found")
	'''Store lyrics of each song along with its source'''	
	lyrics = f"{ly.lyrics} Lyrics provided by {ly.source}"
	return lyrics

def get_song_info(url,sp):
	'''This function will extract all spotify songs from the playlist url
		and make a list of song names and return it'''
	songs = []
	print(" \nGetting all tracks from the Spotify playlist. ")
	playlist_items = None
	playlist_items = sp.playlist_items(url)
	'''Check whether playlist is empty or not'''
	if playlist_items["total"] == 0:
		print(" [x] Spotify playlist was empty. Press any key to exit. \n ")
		input()
		exit()
	else:
		'''Extracting all the songs names from the playlist'''
		tracks = playlist_items['items']
		while playlist_items['next']:
			playlist_items = sp.next(playlist_items)
			tracks.extend(playlist_items['items'])
		songs = []
		for i in tracks:
			artists = []
			for j in i["track"]["artists"]:
				artists.append(j["name"])
			artists = ", ".join(artists)
			title = i["track"]["name"]
			final_title = artists + " - " + title
			songs.append(final_title)
		return songs

def checkCredential():
	'''This function will check credentials to get access of spotify 
	   and thier playlist songs'''
	try:
		api_credentials = open("Related/API_Credentials.json", "r")
		api_data = json.load(api_credentials)
		spotify_client_id = api_data["API_Credentials"]["Spotify_Client_ID"]
		spotify_client_secret = api_data["API_Credentials"]["Spotify_Client_Secret"]
		genius_client_secret = api_data["API_Credentials"]["Genius_Client_Access_Token"]

		if spotify_client_id == "None" or spotify_client_secret == "None" or genius_client_secret == "None":
			print(" [x] Any field in 'API_Credentials.json' is empty. Please read "
				  "'Instructions.txt' before executing the code. Press any key to exit. \n ")
			input()
			exit()
		else:
			auth_manager = SpotifyClientCredentials(client_id=spotify_client_id, client_secret=spotify_client_secret)
			sp = spotipy.Spotify(auth_manager=auth_manager)
			return sp
	except KeyError:
		print(" [x] Seems like 'API_Credentials.json''s key values had been changed. Cannot fetch "
			  "details. Press any key to exit. \n ")
	

'''Main program starts from here'''
print(" \nSpotify Lyrics Extractor\n")
sp=checkCredential()
print("1. Spotify Playlist")
print("2. Spotify Single Track")
choice=input("\nEnter Your Choice:")

if choice=='1':
	'''Sample Url for testing:
	url=https://open.spotify.com/playlist/0PEfws53dtiXkUEvfR2Z2A'''
	url = input(" Enter Spotify Playlist URL: ")
	songs=get_song_info(url,sp) #to get all songs names from the playlist 
	c = 0
	t = len(songs)
	'''Iterate over each song to find its lyrics'''
	for song in songs:
		c += 1
		print(f"\nGetting lyrics for '{song}' [{c} of {t} songs]")
		try:
			lyrics = get_lyrics(song)
			'''To store lyrics in the lyrics folder
			where choosen song lyrics will be save as .txt file'''
			f = open(f"Related/Lyrics/{song}.txt", "w+", encoding='utf-8')
			f.write(lyrics)
			f.close()
			print(" [✓] Successful. ")
		except:
			print("[x] Can't get lyrics, it might happen that the track don't have lyrics. \n ")

if choice=='2':
	'''You can test it with a song like Beggin, Before u go, On my mind etc'''
	spotify_song = input(" Enter Spotify Song Name: ")
	print(f"\nGetting lyrics for {spotify_song}")
	try:
		lyrics = get_lyrics(spotify_song)
		'''To store lyrics in the lyrics folder
			where each song lyrics will be save as .txt file'''
		f = open(f"Related/Lyrics/{spotify_song}.txt", "w+", encoding='utf-8')
		f.write(lyrics)
		f.close()
		print("[✓] Successful. ")
	except:
		print("[x] Can't get lyrics, it might happen that the track don't have lyrics. \n ")

print(f"\n[✓] Successfully all the task is done. Now you can check for the lyrics in 'Lyrics' folder.")






