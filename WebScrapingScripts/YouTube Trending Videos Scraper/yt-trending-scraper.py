from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import pandas as pd

# URLs of the trending pages
urls = [
    "bp=6gQJRkVleHBsb3Jl",
    "bp=4gINGgt5dG1hX2NoYXJ0cw%3D%3D",
    "bp=4gIcGhpnYW1pbmdfY29ycHVzX21vc3RfcG9wdWxhcg%3D%3D",
    "bp=4gIKGgh0cmFpbGVycw%3D%3D",
]

# Opens Chrome
driver = webdriver.Chrome()

# List of scraped video titles
list = []

# Goes to each of the URLs in the urls list and gets the video titles of the top 10 trending videos
for url in urls:
    driver.get(f"https://www.youtube.com/feed/trending?{url}")

    content = driver.page_source.encode("utf8").strip()
    soup = BeautifulSoup(content, "lxml")
    titles = soup.find_all("a", id="video-title")

    for i in range(0, 10):
        print(titles[i].text)
        list.append(titles[i].text)

# Makes a dictionary containing the 4 categories as the keys and the values as the top 10
# trending videos in the section
trending_dict = {
    "Now": list[:10],
    "Music": list[10:20],
    "Gaming": list[20:30],
    "Movies": list[29:39],
}

# Makes a dataframe of trending_dict so that it can be made into an excel file
df = pd.DataFrame(trending_dict)

# Makes the excel file
writer = pd.ExcelWriter("YouTube-Trending.xlsx")
df.to_excel(writer, "Sheet1", index=False)
writer.save()
