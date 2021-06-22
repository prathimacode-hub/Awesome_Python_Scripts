import requests
import json
import os
import time
from bs4 import BeautifulSoup

# Lets find the title of the link
# ......

def getTitle(soup):
    ogTitle = soup.find("meta", property="og:title")

    twitterTitle = soup.find("meta", attrs={"name": "twitter:title"})

    documentTitle = soup.find("title")
    me1Title = soup.find("me1")
    me2Title = soup.find("me2")
    mTitle = soup.find("m")

    res = ogTitle or twitterTitle or documentTitle or me1Title or me2Title or mTitle
    res = res.get_text() or res.get("content", None)

    if (len(res) > 60):
        res = res[0:60]
    if (res == None or len(res.split()) == 0):
        res = "Not available"
    return res.strip()

# to scrape page description


def getDesc(soup):
    ogDesc = soup.find("meta", property="og:description")

    twitterDesc = soup.find("meta", attrs={"name": "twitter:description"})

    metaDesc = soup.find("meta", attrs={"name": "description"})

    pDesc = soup.find("p")

    res = ogDesc or twitterDesc or metaDesc or pDesc
    res = res.get_text() or res.get("content", None)
    if (len(res) > 60):
        res = res[0:60]
    if (res == None or len(res.split()) == 0):
        res = "Not available"
    return res.strip()

# to scrape image link


def getImage(soup, url):
    ogImg = soup.find("meta", property="og:image")

    twitterImg = soup.find("meta", attrs={"name": "twitter:image"})

    metaImg = soup.find("link", attrs={"rel": "img_src"})

    img = soup.find("img")

    res = ogImg or twitterImg or metaImg or img
    res = res.get("content", None) or res.get_text() or res.get("src", None)

    count = 0
    for i in range(0, len(res)):
        if (res[i] == "." or res[i] == "/"):
            count += 1
        else:
            break
    res = res[count::]
    if ((not res == None) and ((not "https://" in res) or (not "https://" in res))):
        res = url + "/" + res
    if (res == None or len(res.split()) == 0):
        res = "Not available"

    return res

# print dictionary


def printData(data):
    for item in data.items():
        print(f'{item[0].capitalize()}: {item[1]}')


# start
print("\nloading.....")
print("- previewing your link -")
print("loading.......\n")

# now, let us get the url from the user
url = input("Enter URL you want to preview : ")

# parsing and checking the url
if (url == ""):
    url = 'www.google.com'
if ((not "http://" in url) or (not "https://" in url)):
    url = "https://" + url

#  let us start printing the values

# first check in the DataBase
db = {}
# create the file if it doesn't exist
if not os.path.exists('linkPreview/db.json'):
    f = open('linkPreview/db.json', "w")
    f.write("{}")
    f.close()

# read db
with open('linkPreview/db.json', 'r+') as file:
    data = file.read()
    if (len(data) == 0):
        data = "{}"
        file.write(data)
    db = json.loads(data)

# let us check if it exists
if (url in db and db[url]["time"] < round(time.time())):
    printData(db[url])
else:
    # if the above is false and if not in db get via request

    # will be getting the html
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")

    sevenDaysInSec = 7*24*60*60
    # let us start printing the data
    newData = {
        "title": getTitle(soup),
        "description": getDesc(soup),
        "url": url,
        "image": getImage(soup, url),
        "time": round(time.time() * 1000) + sevenDaysInSec
    }
    printData(newData)
    # this is parse the file
    db[url] = newData
    with open('Link-Preview/db.json', 'w') as file:
        json.dump(db, file)
print("\n--END--\n")
