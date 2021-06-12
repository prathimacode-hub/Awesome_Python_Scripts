import requests
from termcolor import colored

def color(s,c='g'):
    if(c=='g'):
        return colored(s,"green")
    elif(c=='y'):
        return colored(s,"yellow")       
    elif(c=='c'):
        return colored(s,"cyan")    
    elif(c=='m'):
        return colored(s,"magenta")
    elif(c=='r'):
        return colored(s,"red")    

print(color("\nOMDB API\n",'y'))  
print("1.Search by Movie Title\n2.Search by IMDB ID")
url = "https://www.omdbapi.com/?apikey=<your-api-key>"

#The user is prompted to Enter the input repeatedly until she/he enters the correct option 

while True:
    print(color("\nEnter your option: ",'c'),end=" ")
    opt = int(input())
    
    if(opt==1):
        print(color("\nEnter Movie Title: ",'c'),end=" ")
        title = input()
        url += "t=" + title
        break
    elif(opt==2):
        print(color("\nEnter IMDB ID: ",'c'),end=" ")
        id = input()
        url += "i=" + id
        break
    else:
        print(color("Check your option!!",'r'),end="\n") 
        continue   

#try except block for Exception Handling while performing an API Request
try:
    #The API is requested for the movie information
    response = requests.get(url)
    if(response.ok): #To check if the response was successful
        data = response.json()

        movie_data = "\n"
        movie_data += color('Title: ') + data['Title'] + "\n"
        movie_data += color('Released: ') + data['Released'] + "\n"
        movie_data += color('Genre: ') + data['Genre'] + "\n"
        movie_data += color('Actors: ') + data['Actors'] + "\n"
        movie_data += color('Director: ') + data['Director'] + "\n"                
        movie_data += color('Plot: ') + data['Plot'] + "\n"
        movie_data += color('IMDB Rating: ') + data['imdbRating'] + "\n"

        # The string "N/A" is replaced to provide a meaningful information to the user
        movie_data = movie_data.replace("N/A","Data not available")
        print (movie_data)

except:
    if(data['Response']=="False"):
        error = color("\n"+data['Error'],'r')
        print(error)