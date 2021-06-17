#pip install IMDbPY
import imdb


a = imdb.IMDb()
#getting name of movie from user
movie_name = input("Enter the name of Movie : ")
movie = a.search_movie(str(movie_name))
index = movie[0].getID()
movie = a.get_movie(index)

movie_title = movie['title']
movie_year = movie['year']
movie_cast = movie['cast']
list_of_cast = ','.join(map(str, movie_cast))

#printing all the data fetched
print("Title of the movie is : ", movie_title)
print("Year of the release of the movie is : ", movie_year)
print("Full cast of the movie : ", movie_cast )