# Twitter API
## Short Description:
**Imported Libraries:**
- tweepy
- pandas
- csv


**Purpose:**
It can extract tweets from a specific user or using a specifc keyword.

**Steps Taken:**
- Retrieved API tokens from twitter develepor account.
- Added them to a csv file, saved it on drive and used tokens by specifying the path.
- Twitter has a rate limit of about 900 tweets/15 minutes (could vary), it gives an error if you exceed it, hence added code to handle the error
- Created function user_tweets, which uses api.user_timeline to extract tweets from a specific user.
- Created function keyword_tweets, which uses api.search to extract tweets using a search query, i.e a keyword.
- Wrote the extracted tweets in a csv file, which gets created and saved in drive automatically.
- The main driver function: gave user option to choose how they wished to extract tweets and executed the code.
- Printed the hence created csv file.

------------
## Setup Instructions:
1. Get a twitter developer account by registering at [https://developer.twitter.com/en](https://developer.twitter.com/en)
2. Mount Google drive
3. Run the code.

------------

## Output:
![Covid csv file img](https://github.com/pragyakhanna11/Awesome_Python_Scripts/blob/dc78bbbc72cde791ffd1cc608fe7458043a1c31c/APIScripts/Twitter%20API/Images/covid_csv.png)


------------

## Author:
Pragya Khanna
