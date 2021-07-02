# Import the following modules
from pushbullet import PushBullet  # pip install pushbullet.py==0.9.1
from pywebio.input import *  # pip install pywebio
from pywebio.output import *
from pywebio.session import *
import time

# Get the access token from Pushbullet.com
access_token = "o.0B1PXovD38JIvPcxnIFsTliAipgQiML1"


# Taking input from the user
data = input('Title', PlaceHolder="Title")
# Taking large text input from the user
text = textarea("Text", rows=3,
                placeholder="Write something...", required=True)
# Get the instance using access token
pb = PushBullet(access_token)
# Send the data by passing the main title and text to be send
push = pb.push_note(data, text)
# Put a success message after sending the notification
put_success("Message sent successfullly...")
time.sleep(3)  # S,leep for 3 seconds
clear()  # Clear the screen
toast("Thanks for using it :)")  # Give the pop at last
hold()  # hold the session untill the whole work finishes
