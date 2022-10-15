# HTML Page Read and Upload
# Import useful libraries and classes.

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

# html page upload and read in web_page variable.
my_url=  "https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1"
web_page= uReq(my_url)
page_html= web_page.read()

# Parsing
# html parser. It is to beautify the HTML code.
page_soup= soup(page_html)

# Extraction of information
# read class attribute from web page in containers variable.
# Print the length of containers.

containers= page_soup.findAll("div", {"class": "_2kHMtA"})
print(len(containers))

# Extracting Product Name
# The product_name_list contains the name of product extracted using find function using div tag and
# class name

product_name_list = []

for box in containers:
    # name of product is extracted using div tag with class name as given in website
    product_name = box.find("div", class_="_4rR01T")
    # the extracted names is stored in a list
    product_name_list.append(product_name.string)

# Extracting Ratings
# The rating_list contains the ratings of product extracted using find function using div tag and class name

rating_list = []

for box in containers:
    # rating of product is extracted using div tag with class name as given in website, if the rating is None, then 0.0 is used.
    rating = box.find("div", class_="_3LWZlK")
    if rating != None:
        rating_list.append(rating.text)
    else:
        rating_list.append('0.0')
# Extracting Price of Product
# The price_list contains the price of product extracted using find function using div tag and class name
price_list = []

for box in containers:
    # price of product is extracted using div tag with class name as given in website
    price = box.find("div", class_="_30jeq3")
    # the extracted price is stored in a list after string Rupees sign.
    price_list.append(price.string.strip('₹'))

# The container in website contains a list of information of the product which is
# extracted using find function using li tag and class name
# here n is length of containers in 1 page.

n = len(containers)

# list to store RAM of phones
ram_list = []
# list to store ROM of phones
rom_list = []
# list to store Display Screen of phones
display_list = []
# list to store Camera Specification of phones
camera_list = []
# list to store Battery Life of phones
battery_life_list = []
# list to store Warranty Period of phones
warranty_list = []
# temporary list to store the all the list of phones's specifications
temp_list = []


for box in containers:
    # one list out of all product list is extracted using li tag with class name as given in website
    temp_box = box.findAll("li", class_="rgWa7D")
    temp_list.append(temp_box)

for i in range(n):
    # this loop extracts the values stored in the list of one container.
    # since in the website the RAM & ROM of phoes are listed together
    # so it is stored in a list and then splitted as per given splittor element.
    split_list = temp_list[i][0].string.split('|')
    # the extracted RAM is stored in a list
    ram_list.append(split_list[0])
    # the extracted ROM is stored in a list
    rom_list.append(split_list[1])
    # the extracted display is stored in a list
    display_list.append(temp_list[i][1].string)
    # the extracted camera is stored in a list
    camera_list.append(temp_list[i][2].string)
    # the extracted battery is stored in a list
    battery_life_list.append(temp_list[i][3].string)
    # the extracted warranty is stored in a list
    warranty_list.append(temp_list[i][-1].string)

# Creating Pandas DataFrame from Data scraped from Web
# Importing Pandas to create a DataFrame
import pandas as pd
# Creating a Dictionary to store List values and creating DataFrame
dictionary = {'Product_Name':product_name_list, 'Ratings':rating_list, 'Price':price_list, 'RAM_Storage':ram_list,
              'ROM_Storage':rom_list, 'Display_Screen':display_list, 'Camera':camera_list, 'Battery_Life':battery_life_list,
              'Warranty_Life':warranty_list}
dataframe = pd.DataFrame(dictionary)
# Head of DataFrame
dataframe.head()

# Tail of DataFrame
dataframe.tail()
