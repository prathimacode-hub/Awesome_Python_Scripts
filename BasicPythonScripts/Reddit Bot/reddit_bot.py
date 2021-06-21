# imporing the libraries for this project. Check the requirements.txt file
import praw
import config
import time
import os

# login details fetched by the bot
# takes all the details of the config.py
def bot_login():
	print "Logging in..."
	r = praw.Reddit(username = config.username,
				password = config.password,
				client_id = config.client_id,
				client_secret = config.client_secret,
				user_agent = "The Reddit Commenter v1.0")
	print "Logged in!"

	return r

# searching previous 1000 comments and checking whether they are eligible to comment out
def run_bot(r, comments_replied_to):
	print "Searching last 1,000 comments"

	for comment in r.subreddit('test').comments(limit=1000):
		if "sample user comment" in comment.body and comment.id not in comments_replied_to and comment.author != r.user.me():
			print "String with \"sample user comment\" found in comment " + comment.id
			comment.reply("Hey, I like your comment!")
			print "Replied to comment " + comment.id
			# If the client server matches then it will comment and the comment id will be shown
			comments_replied_to.append(comment.id)
			# The replied comment will be stored in the comments_replied_to.txt file automatically
			with open ("comments_replied_to.txt", "a") as f:
				f.write(comment.id + "\n")

	print "Search Completed."

	print comments_replied_to

	print "Sleeping for 10 seconds..."
	#Sleep for 10 seconds...		
	time.sleep(10)
# Search operation completed and as well as the comment are done


# function created for saving the comments
def get_saved_comments():
	if not os.path.isfile("comments_replied_to.txt"):
		comments_replied_to = []
	else:
		with open("comments_replied_to.txt", "r") as f:
			comments_replied_to = f.read()
			comments_replied_to = comments_replied_to.split("\n")
			comments_replied_to = filter(None, comments_replied_to)

	return comments_replied_to

r = bot_login()
comments_replied_to = get_saved_comments()
print comments_replied_to

# creating the infinte loop for the project
while True:
	run_bot(r, comments_replied_to)
