# Overview
We will be scraping data from Flipkart website and then will use the data to create a DataFrame, which used for data analysis.

## Web-Scraping
       Web scraping is an automatic method to obtain large amounts of data from websites. 

       Most of this data is unstructured data in an HTML format which is then converted into structured data in a spreadsheet or a 
       database so that it can be used in various applications.
       
## Data Frame
       A data frame is a table or a two-dimensional array-like structure in which each column contains values of one variable 
       and each row contains one set of values from each column.
       
## Python Libraries Required

- BeautifulSoup - It has been used to extract the HTML elements from website.
- Urllib - It has been to send and recieve the request in order to fetch the data from FlipKart.
- Pandas - It is used to create and store dataframes into .csv format.

## Setup Packages
 - pip install requests
 - pip install pandas
 - pip install bs4

## Workflow
1. Go to the url : <a href = 'https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&wid=1.productCard.PMU_V2_1'> FlipKart Samsung Mobiles </a>


<img width="631" alt="image" src="https://user-images.githubusercontent.com/76874762/194710211-de97ec25-1e4a-432e-9c41-edb2e3660b64.png">



2. Right click to Inspect & Hover over to see the HTML code.

<img width="902" alt="Screenshot_20221008_070628" src="https://user-images.githubusercontent.com/76874762/194710338-3b62fd8a-31da-4e2d-8552-14d8ba6953f1.png">


3. Import libraries to start scraping web data

4. Hover over elements you want to scrape data from and use BeautifulSoup library methods to extract data from tags and class names.

5. Create a Dataframe from extracted data and proceed for further analysis.


## Output
<img width="602" alt="image" src="https://user-images.githubusercontent.com/76874762/194710541-a29228c9-e3e0-41e2-a120-17e2968f7ad8.png">

### Author

<a href='https://singhmansi25.github.io'> Mansi Singh </a>
