# **Here I shall be showing you how to do web scraping using BeautifulSoup, on the website [toscrape.com](https://quotes.toscrape.com/)**

# **This website is made just to practice web scrapping only**


# Install required libraries
# !pip install beautifulsoup4
# !pip install requests

import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')


# **Extracting the title of the website first**

title = soup.title
print(title)


# **Here, we can clearly see that, instead of just the title of the website, it is extracting the whole title tag, we can extract title using ```.text``` method**

print(title.text)


# **NOTE:-** ``` In order to scrape more data from the website, you need to know the basics of HTML and CSS, you just need to know what are classes, tags and other such basic terms :)```

# **In order to scrape more data, you need to understand what element lies in which tag, so just Right Click on the web page and click on 'Inspect', you will get a HTML page and you will be able to see which element lies in which tag**

# ### Scraping the header

# **Using ```find``` method**

print(soup.find('h1').text.strip())

# **Using ```CSS-Selectors```**

print(soup.select_one('.col-md-8 > h1').text.strip())

# There are many different methods to scrape the same element from the websites like:
#  - Using Find Method
#  - Using CSS Selectors
#  - Extracting children from parent element
#  - Extracting siblings of an element

# **In this notebook, I shall be using ```CSS-Selectors``` and ```Find``` method only as they are easier to understand**

# ### Extracting the first Quote

# **The very first quote lies in the class named "text"**

print(soup.find(class_ = "text").text.strip())

quotes = soup.find_all(class_ = 'text')
quotes


# **Here it is giving all the tags having the class = "text", in the form of a list but we want quotes only**

# **Extracting quotes text from the above list**


for quote in quotes:
    print(quote.text,"\n")


# **Scraping Author names of each quote in the same manner** 


# soup.select('.author') CSS selector of the same output
authors = soup.find_all(class_ = 'author')
authors

for author in authors:
    print(author.text)

# **In the same manner, those tags of each quote can be extracted, you can do that by yourself :)**

# ### **Now let's try to extract the data from multiple pages**

print(soup.select_one(".next > a"))

# **We can clearly see that each page contains a ```Next``` button which contains the class called next which fuurther contains the link of next page**

# **We can also observe that how the link is changing when we are changing the page**

authors_lst = []
quotes_lst = []
tags_lst = []

page = 1
next_button = True

while next_button: # If a web page contains next_button tag then the value of page will increase by 1 and 
                    # the data would be extracted from next page
    response = requests.get("https://quotes.toscrape.com/page/"+str(page))
    soup = BeautifulSoup(response.text, 'html.parser')
    
    quotes = soup.find_all(class_ = 'quote')# All the info about quote, its author and related tags is in this class
    for quote in quotes:
        all_tags = []
        text = quote.select_one('.text').text
#         print(text)
        quotes_lst.append(text)
        
        author = quote.select_one('.author').text
#         print(author)
        authors_lst.append(author)
    
        tags = quote.find_all(class_ = 'tag')
#         print(tags[0])
        for tag in tags:
#             print(tag.text)
            all_tags.append(tag.text)
        tags_lst.append(all_tags)
        
#     print(page)
    next_button = soup.select_one(".next > a")
    page+=1


# **Now let's create a dataframe of the extracted data**


records = {} # Creating a dictionary to store all the data
records['Quote'] = quotes_lst
records['Author'] = authors_lst
records['Tags'] = tags_lst


import pandas as pd
df = pd.DataFrame(records) # Converting that dictionary into dataframe

print(df.head(10))

#df.to_csv('Quotes.csv', index=False) # Getting the data in the form of CSV file
