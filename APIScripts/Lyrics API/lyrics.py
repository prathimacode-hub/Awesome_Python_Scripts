import lyricsgenius
import os
genius = lyricsgenius.Genius("ZEH3ldCCxE3Eh9Vce2MAzc_b4Rf_KIZCh1LJBoXEnWkmEGWpX4EBr9Z8bqno2-Ko")
#genius.verbose = False

artistName = "Andy Shauf"
songName = "Alexander All Alone"

artistName = input("Enter Artist Name :")
songName = input("Enter Song Name :")

artist = genius.search_artist(artistName, sort="title", max_songs=3)
song = artist.song(songName)

try:
    os.mkdir("D:/React_apps/Lyrics Downloader/Lyrics")
except:
    pass
    
path = 'D:/React_apps/Lyrics Downloader/Lyrics/lyrics.txt'
file=open(path, "w+")
file.write(str(song.lyrics))
print(song.lyrics)
file.close()
