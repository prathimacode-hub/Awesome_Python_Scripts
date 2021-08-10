# Internship-Internshala Web Scrapping

## Aim

To create a python script using Beautifulsoup module to work with popular internship website - Internshala, and extract the internship details by filtering our needs.

## Purpose

The purpose of this project is to create a internship searching useful for students to find their internship.

## Short description of package/script

- If standalone script, short description of script explaining what it achieves.

   Include work from home
     - Part-time
     - Internships for women
     - Internships with job offer
     - Starting from (or after)
     - Max Duration
     - select multiple locations
     - select multiple Category

- List out the libraries imported.
  - `requests` [To fetch the Url content ]
  - `BeautifulSoup4` [Library used for web scraping]
  - `xlwt` [To export the data to a Excel File with multiple sheets]

## Setup instructions

1. Download or clone the repository
2. Install Required Libraries
3. Run main.py 
4. Provide appropriate input
5. Obtain the excel file in .xls format

##  Input Work Flows 
```
Include Work From home?
Include Part-time?
Internships for women?
Internships with job offer?
(Represent your choice with 1-True or 0-False separated by commas such as 1,0,0,1)

1,0,0,0
Enter different categories separated by commas* (Required)
Web Development
Enter different locations separated by commas* (Required)
Mumbai,Delhi
Enter start date in format (yyyy-mm-dd) or leave empty for current date

Enter maximum duration or leave empty for any duration
3
--------------------------------------------------------------------
How many pages you would like to get? Max Pages (16)
2
Different pages on different sheets?(Default: Yes) | 1: No
#Leave empty if Yes 
--------------Scraping Page 1 -----------------
--------------Scraping Page 2 -----------------

1: Add New Sheet
2: Save and Open the file in Excel
3: Save file
4: Discard file and Exit
2
Enter the name of the file
Web_Dev
```

## Output

![](https://github.com/rammya29/Awesome_Python_Scripts/blob/main/WebScrapingScripts/Internship-Internshala/Images/Internshala%20logo.jpg)

![](https://github.com/rammya29/Awesome_Python_Scripts/blob/main/WebScrapingScripts/Internship-Internshala/Images/Screenshot%201.png)

![](https://github.com/rammya29/Awesome_Python_Scripts/blob/main/WebScrapingScripts/Internship-Internshala/Images/Screenshot%202.png)

## Author(s)

Rammya Dharshini K

## Disclaimers, if any

None
