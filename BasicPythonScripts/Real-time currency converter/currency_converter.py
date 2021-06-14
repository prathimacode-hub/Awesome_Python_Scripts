from forex_python.converter import CurrencyRates, CurrencyCodes


rates = CurrencyRates()

codes = CurrencyCodes()


def exchange_rate():
     c1 = input("Enter country code one (from): ").upper()
     c2 = input("Enter country code two (to): ").upper()
     print(rates.get_rate(c1, c2))

def conversion():
     t1 = input("Enter country code one (from): ").upper()
     t2 = input("Enter country code two (to): ").upper()
     t3 = int(input("Enter the amount of currency in " + t1 + " :"))

     print(rates.convert(t1, t2, t3))

def other():
     s1 = input("Type sym for symbols or name for currency name: ")
     if s1 == 'sym':
        s2 = input("Enter the currency code of the country: ").upper()
        print(codes.get_symbol(s2))
     elif s1 == 'name':
        s3 = input("Enter the currency name: ").upper()
        print(codes.get_currency_name(s3))

while True:
    purpose = input("Type 'r' if you wish to know the rate of currency, 'c' for converting currency or 's' for alternate information: ")

    try:
         if purpose == 'r':
            exchange_rate()
         elif purpose == 'c':
            conversion()
         elif purpose == 's':
            other()
            break
         print("Enter only r,c or s")

    except:
         continue
