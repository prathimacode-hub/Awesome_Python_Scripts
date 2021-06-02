from newsapi import NewsApiClient
import pycountry


def Check(input_countries):
    input_countries = [input_countries.strip()]

    countries = {}
    for country in pycountry.countries:
        countries[country.name] = country.alpha_2

    codes = [countries.get(country.title(), 'NO')
             for country in input_countries]
    if codes[0] == "NO":
        return "Country not found, Try searching..."
    return None


if __name__ == "__main__":
    while 1:
        newsapi = NewsApiClient(api_key='0864a52124954666bb3e1fd0f7fbb1e6')

        input_country = input("Country: ")
        input_countries = [f'{input_country.strip()}']

        countries = {}

        for country in pycountry.countries:
            countries[country.name] = country.alpha_2

        codes = [countries.get(country.title(), 'Unknown code')
                 for country in input_countries]

        option = input(
            "Which category are you interested in?\n1.Business\n2.Entertainmen\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
        top_headlines = newsapi.get_top_headlines(
            category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')

        Headlines = top_headlines['articles']
        if Headlines:
            for articles in Headlines:
                b = articles['title'][::-1].index("-")
                if "news" in (articles['title'][-b+1:]).lower():
                    print(
                        f"{articles['title'][-b+1:]}: {articles['title'][:-b-2]}.")
                else:
                    print(
                        f"{articles['title'][-b+1:]} News: {articles['title'][:-b-2]}.")
        else:
            print(f"No articles found for {input_country}, Try for others...")
        option = input("Do you want to search again[Yes/No]?")
        if option == 'Yes':
            continue
        else:
            exit()
