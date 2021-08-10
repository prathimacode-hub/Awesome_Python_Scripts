import lyricsgenius #importing api
import os
genius = lyricsgenius.Genius("ZEH3ldCCxE3Eh9Vce2MAzc_b4Rf_KIZCh1LJBoXEnWkmEGWpX4EBr9Z8bqno2-Ko") #unique access key is passed
genius.verbose = False #dont show song names

artistName = "Andy Shauf"
songName = "Alexander All Alone"

artistName = input("Enter Artist Name :")
songName = input("Enter Song Name :")

artist = genius.search_artist(artistName, sort="title") #search all song by artist
song = artist.song(songName) #search particular song

try:
    os.mkdir("D:/React_apps/Lyrics Downloader/Lyrics") #make directory if not available
except:
    pass
    
path = 'D:/React_apps/Lyrics Downloader/Lyrics/lyrics.txt' #specify path here
file=open(path, "w+")
file.write(str(song.lyrics)) #write song to file
#print(song.lyrics)
file.close() #close file
