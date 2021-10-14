##Crypto Price Checker

## Aim

To fetch live top-100 cryptocurrency prices scraped from cointracker.io

## Purpose

Instead of users manually looking for live prices they can run the script easily to get the prices of cryptocurrencies.

## Short description of package/script

- The script navigates to website "https://www.cointracker.io/price" and then finds out the top 100 cryptocurrencies on that
  webpage and then prints the price of all the cryptocurrencies in that webpage.
- Libraries imported : requests, bs4 (beautiful soup).


## Workflow of the Project

I am getting the data from website "https://www.cointracker.io/price" and in this site there are tags with class name 
"d-flex no-underline" and for all 100 cryptocurrencies I am finding this class and storing the "price/<cryptocurrency>" in the list 
and then looping through the list and then navigating to website "https://www.cointracker.io/" + "price/<cryptocurrency>". Then I am
finding the div tag with class name "my-auto h4" and then converting the data received to string. Then I am finding the first index 
of price string and looping till the end of price string. Then for each cryptocurrency I am printing it's name and it's price.


## Setup instructions

Just press "run" on IDLE or write "python crypto_price_checker.py" on command prompt.


## Detailed explanation of script, if needed

Explained above


## Compilation Steps

Explained above

## Author(s)

Varun Kumar


## Disclaimers, if any

Use this section to mention if any particular disclaimer is required
