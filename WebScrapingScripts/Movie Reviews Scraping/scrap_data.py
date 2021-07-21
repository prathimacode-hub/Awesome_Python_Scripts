# Import important packages that are used to fetch the details of the movies.

from bs4 import BeautifulSoup
import requests
import pandas
import json


# Enter the url from where you want to fetch the Movie data
# In this Program we have fetch data from IMDB.
# Here, we will collect data from top-rated movies on IMDB and most popular movies upto date 21 July 2021.
# There are approx 250 top- rated movies on IMDB, and 100 most popular movies, here are a total of 350 movies


# urls
top_rated_movies = "https://www.imdb.com/chart/top"
most_popular_movies = "https://www.imdb.com/chart/moviemeter/"


# ---------------------------------------------------------------------------------------------------------------------------
def get_movies_list(url):
    """
    This function will help us to get the list of movies that are present in the given url
    This function takes an input url, and get the list of all movies present in the url.
    It  will return the movies with its corresponding rating and links, so that we can
    get our review.

    Return Type : Dictionary
    because we have make seperate link and rating for each movie, so that we don't get confuse while watching the data.
    If we use list instead of dict, we won't understand what is there in the data.
    """

    # sending request to access the particular url
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'lxml')
    content = soup.find_all('tbody', class_ = "lister-list")
    
    # We have got our movie names using list comprehension
    movies_names = [content[0].find_all('tr')[i].find('td', class_ = "titleColumn").a.text for i in range(len(content[0].find_all('tr')))]
    
    # here we have not use list comprehension because there are some movies which don't have their ratings
    rating = []
    for i in range(len(content[0].find_all('tr'))):

        try:
            rating.append(content[0].find_all('tr')[i].find('td', class_ = "ratingColumn imdbRating").strong.text)
        except:
            # Here, we mark that rating will be empty if no rating is present, later while performing any task,
            # we will fill this value by proper techniques 
            rating.append(" ")

    # Links for each movie
    links = [content[0].find_all('tr')[i].find('td', class_ = "titleColumn").a['href'] for i in range(len(content[0].find_all('tr')))]

    # here we have created movies dictonary in which all the data of each movie is present.
    movies = {}
    for i in range(len(content[0].find_all('tr'))):
        if movies.get(movies_names[i]) is None:
            movies[movies_names[i]] = {}
            link = "https://www.imdb.com" + links[i]
            movies[movies_names[i]] = (rating[i], link)
        else:
            link = "https://www.imdb.com" + links[i]
            movies[movies_names[i]] = (rating[i], link)


    return movies  # Return type: DICT



# ---------------------------------------------------------------------------------------------------------------------------
def fetch_data(movies):
    """
    This function will give us the reviews about the movies that we have got in our get_movies_list().
    It will take input a movies dictionary in which movies and its links are present

    It will return a list of reviews, in which reviews are in the form of tuple.
    e.g-> review = [('6',
                    'Average Marvel Movie',
                    'As the perspective is everything in reviewing movies)]

            rating = review[0][0]
            title = review[0][1]
            review_content = review[0][2]
    """
    reviews = list()
    for key, val in movies.items():

        # sending request to access the particular url
        movie_url = val[1]
        print("Getting Data of Movie : {}".format(key))
        response = requests.get(movie_url)
        soup = BeautifulSoup(response.content, 'lxml')
        content = soup.find_all('section', class_ = "ipc-page-section ipc-page-section--base")
        
        review_url = soup.find_all('a', class_ = "ipc-title ipc-title--section-title ipc-title--base ipc-title--on-textPrimary ipc-title-link-wrapper")
        review_url = "https://www.imdb.com" + review_url[2]['href']
        
        review_url_response = requests.get(review_url)
        review_url_soup = BeautifulSoup(review_url_response.content, 'lxml')
        
        # here we have got several reviews from a single movie.
        total_reviews = review_url_soup.find_all('div', class_ = "review-container")
        # here, it made us necessary to iterate a loop, because it contains several reviews, and every review is important to us.
        for review in total_reviews:
            # using exception handling in case, if there is no title or review or rating is not present.
            try:
                rating = review.find("div", class_ = "ipl-ratings-bar")
                rating = rating.find('span').text.strip().split("/")[0]
            except:
                rating = " "
            try:
                title = review.find('a', class_ = "title").text.strip()
            except: 
                title = "NaN"
            try:
                review_content = review.find('div', class_ = "text show-more__control").text.strip()
            except:
                review_content = None
            

            # Appending data to the list
            reviews.append((rating, title, review_content))
        
    print("Total Reviews Fetch from the data are : {}".format(len(reviews)))
    
    return reviews # return type: list of tuples



# ---------------------------------------------------------------------------------------------------------------------------
def to_csv(reviews,flocation : str = "", return_data = True):
    """
    It will make the dataframe of the reviews and present us, it will easily able to understand and read the data,
    and main aim of this function is to save the data in csv format, 

    : If we don't enter the file location, it will automatically store the data into existing file with the name 
      as "data.csv"

    : If we don't want to return the data, we won't by entering return_data = False
    """
    dataFrame = pd.DataFrame(data = reviews, columns = ['Rating', 'Title', 'Review'])
    
    if flocation:
        dataFrame.to_csv(flocation)
    else:
        dataFrame.to_csv("data.csv")
        
    if return_data:
        return dataFrame
    else:
        pass




# ---------------------------------------------------------------------------------------------------------------------------
def to_json(movies, fname : str = ""):
    """
    A helper function which is used to save the movies name and its links.
    """
    with open(fname, 'w') as file:
        json.dump(movies, file)



# ---------------------------------------------------------------------------------------------------------------------------
def selectMovie(**kwargs):
    #**kwargs creates a dictionary so to fetch the data we have dictionary concept to get data
    for key, val in kwargs.items():

        # If we want get data from top-rated movies
        if key == "top_rated_movies" and val == True:
            # fetch data from top-rated movies
            movies = get_movies_list(top_rated_movies)
            reviews = fetch_data(movies = movies)
            to_csv(reviews = reviews,flocation = "datasets/reviews_top-rated.csv" ,return_data=False)
        
        # If we want to get the data from most-popular movies
        elif key == "most_popular_movies" and val == True:
            # fetch data from most-popular movies
            movies = get_movies_list(most_popular_movies)
            reviews = fetch_data(movies = movies)
            to_csv(reviews = reviews,flocation = "datasets/reviews_most-pop.csv" ,return_data=False)
        
        




if __name__ == "__main__":
    # here we will fetching both the data from the IMDB
    selectMovie(top_rated_movies = True)
    selectMovie(most_popular_movies = True)

