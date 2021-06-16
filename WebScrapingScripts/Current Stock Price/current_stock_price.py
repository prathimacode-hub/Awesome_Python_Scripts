# import the requests module to call the url
import requests

# import the BeautifulSoup module for web scraping the elements and data
from bs4 import BeautifulSoup


# Define a function which returns the data calling the url and accessing classes
def stock_price(symbol: str = "AAPL") -> str:
    url = f"https://in.finance.yahoo.com/quote/{symbol}?s={symbol}"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    class_ = "My(6px) Pos(r) smartphone_Mt(6px)"
    return soup.find("div", class_=class_).find("span").text


if __name__ == "__main__":
    # Iterate using for loop where those words are found
    for symbol in "AAPL AMZN IBM GOOG MSFT ORCL ABM A".split():
        # Print the output after fetching data
        print(f"Current {symbol:<4} stock price is:  {stock_price(symbol):>8}")
