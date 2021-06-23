from newsapi import NewsApiClient  # pip install newsapi-python
import pycountry  # pip install pycountry


# Fucntion to check whether Country is exists or not.
def Check(input_countries):
    input_countries = [input_countries.strip()]

    countries = {}
    for country in pycountry.countries:
        # store all the alpha_2 values of all the countries
        countries[country.name] = country.alpha_2

    codes = [countries.get(country.title(), 'NO')
             for country in input_countries]  # Check that your input country have any alpha_2 code or not.
    if codes[0] == "NO":
        return "Country not found, Try searching..."
    return None


if __name__ == "__main__":
    while 1:
        # Get your API key from New API
        newsapi = NewsApiClient(api_key='Your API Key')

        input_country = input("Country: ")  # Taking country name input
        input_countries = [f'{input_country.strip()}']

        countries = {}

        for country in pycountry.countries:
            countries[country.name] = country.alpha_2

        codes = [countries.get(country.title(), 'Unknown code')
                 for country in input_countries]  # If code is not found means Unknown code
        # Choose Category of the news.
        option = input(
            "Which category are you interested in?\n1.Business\n2.Entertainment\n3.General\n4.Health\n5.Science\n6.Technology\n\nEnter here: ")
        top_headlines = newsapi.get_top_headlines(
            category=f'{option.lower()}', language='en', country=f'{codes[0].lower()}')  # getting top headlines from all the news channels

        Headlines = top_headlines['articles']  # fetch the top articles
        if Headlines:
            # For storing content in a Good manner
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
        if option.lower() == 'yes':
            continue
        else:
            exit()
