# Import following modules
import urllib.request
import pandas as pd  # pip install pandas
from pushbullet import PushBullet  # pip install pushbullet.py == 0.9.1

# Note: pip install openpyxl - Install this module

# Get Access Token from pushbullet.com
Access_token = "o.aUTXEomlNPUbJQpdzl4YxQjybOSE0uRz"
pb = PushBullet(Access_token)  # Authentication

all_pushes = pb.get_pushes()  # All pushes created by you
latest_one = all_pushes[0]  # Get the latest push
url = latest_one['file_url']  # Fetch the latest file URL link

Text_file = "All_Chats.txt"  # Create a new text file for storing all the chats
# Retrieve all the data store into Text file
urllib.request.urlretrieve(url, Text_file)

chat_list = []  # Create an empty chat list

# Open the Text file in read mode and read all the data
with open(Text_file, mode='r', encoding='utf8') as f:
    data = f.readlines()  # Read all the data line-by-line

# Excluded the first item of the list, coz first items contains some garbage data
final_data_set = data[1:]

# Run a loop and read all the data line-by-line
for line in final_data_set:
    date = line.split(",")[0]  # Extract the date
    tim = line.split("-")[0].split(",")[1]  # Extract the time
    name = line.split(":")[1].split("-")[1]  # Extract the name
    messag = line.split(":")[2][:-1]  # Extract the message
    # Append all the data in a List
    chat_list.append([date, tim, name, messag])

# Create a dataframe, for storing all the data in a excel file
df = pd.DataFrame(chat_list, columns=['Date', 'Time', 'Name', 'Message'])
df.to_excel("BackUp.xlsx", index=False)
