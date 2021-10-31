import requests
import bs4

url = "https://www.cointracker.io/price"
req = requests.get(url)
scrap = bs4.BeautifulSoup(req.text, 'html.parser')

#getting list of individual sites to get price data
individual_sites = [tag['href'] for tag in scrap.find_all('a', {'class':"d-flex no-underline"})]

for i in range(len(individual_sites)):
	#appending the string for each "i" to "https://www.cointracker.io".
	url2 = "https://www.cointracker.io" + individual_sites[i]
	req2 = requests.get(url2)
	scrap2 = bs4.BeautifulSoup(req2.text, 'html.parser')

	#getting the cryptocurreny name from the string
	crypto_name = individual_sites[i][7:]

	#getting the data where the price is present and converting it to string
	findClass = scrap2.find('div', {'class':'my-auto h4'})
	findClassStr = str(findClass)
	
	#finding index from which price of cryptocurrency starts
	idx = findClassStr.find("data-price-container-symbol=")
	idx = findClassStr.find(">", idx, len(findClassStr))
	idx = idx+1
	price_str = ""

	#looping till I get the complete price as a string
	while(findClassStr[idx]!="<"):
		price_str = price_str + findClassStr[idx]
		idx = idx+1
	print("crptocurrency : " + crypto_name + " and 1 " + crypto_name + " = " + price_str)
	

