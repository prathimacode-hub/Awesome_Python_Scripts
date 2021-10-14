import pyshorteners #library in python for shortening URL
def shorten(url):
    return pyshorteners.Shortener().tinyurl.short(url) ## shortening the URL

url = input("Enter URL: ") #takes input(URL) from the user
print("Shortened URL : ", shorten(url)) #returns output