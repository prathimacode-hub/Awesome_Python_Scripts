import requests
req=int(input("Enter number of requests  "))
print("Enter currency: \n e.g. Bitcoin\n Ethereum \n Dogecoin \n Litecoin \n Cardano \n Stellar  \n Polkadot \n  ")
for i in range(req):
    url='https://cryptantapi.root.sx/getPrice/'
    a=input("Enter currency \n")
    print("----------------------------------------------------------------------------------")
    url+=a
    response = requests.get(url)
    status_code = response.status_code
    if status_code == 200:
       
        print( "Currency: ", a)
        print( "Price in USD: ",response.json()['priceUsd'],'$')
        print( "Percentage change in 24 hrs: ",response.json()['percentChange24hUsd'],'%')
        print( "last updated: ",response.json()['lastUpdated'][:10])
    else:
        print("Enter valid currency")
        
print("Done")