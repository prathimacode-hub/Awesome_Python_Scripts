from bs4 import BeautifulSoup
from datetime import datetime
from datetime import date
import time
import pandas as pd
import requests

c = 0
# some coin names to be scraped.
CoinsNames = ["Bitcoin-USD", "Ethereum-USD", "HEX-USD", "Cardano-USD", "Tether-USD"]

while True:
    now = datetime.now()
    current_time = str(
        now.strftime("%H:%M:%S") + " " + str(date.today())
    )  # this is just to get the time at the time of web scraping
    print(f"At time : {current_time} IST")

    # url to be scraped.
    url = "https://finance.yahoo.com/cryptocurrencies/"
    response = requests.get(url, headers={"Referer": "https://finance.yahoo.com/"})

    text = response.text
    html_data = BeautifulSoup(text, "html.parser")
    headings = html_data.find_all("tr")[0]
    headings_list = []
    for x in headings:
        headings_list.append(x.text)

    headings_list = headings_list[2:10]
    headings_list.insert(0, "Date & Time")

    # path for the csv files, which needs to be changed as per the user.
    path = "D:\hacktoberfest\General-Purpose-Scripts\scripts\CryptoCurrencyTracker\CoinsData"
    datum = {}
    if c == 0:
        datum = {}
        c += 1

    else:
        for coin in CoinsNames:
            try:
                df = pd.read_csv(path + "\\" + coin + ".csv")
            except:
                df = pd.DataFrame()

            datum[coin] = df

    for x in range(1, 6):
        rows = html_data.find_all("tr")[x]
        column_value = rows.find_all("td")
        row = []
        for i in range(10):
            row.append(column_value[i].text)

        name = row[1].replace(" ", "-")
        row = row[2:]
        row.insert(0, current_time)

        if name not in datum.keys():
            datum[name] = pd.DataFrame([row], columns=headings_list)

        else:
            temp = pd.DataFrame([row], columns=headings_list)
            print(row)
            datum[name] = pd.concat([datum[name], temp])

    # To write to the csv files.
    for eachone in datum.keys():
        newpath = path + "\\" + eachone + ".csv"
        datum[eachone].to_csv(path + "\\" + eachone + ".csv", index=False)

    # to delete the response and creae a new instance
    del response
    time.sleep(600)
