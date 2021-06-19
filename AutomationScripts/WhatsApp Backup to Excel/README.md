![](http://ForTheBadge.com/images/badges/made-with-python.svg)
![](https://forthebadge.com/images/badges/built-by-developers.svg)</br>
[![Prettier](https://img.shields.io/badge/Code%20Style-Prettier-red.svg)](https://github.com/prettier/prettier)
![License](https://img.shields.io/badge/License-MIT-red.svg)</br>

## Description: 
- We'll utilize many Python modules and frameworks to export the conversations. We'll make four columns in the excel file: date, time, name, and message. 
- We'll use Pandas to construct these columns, export all of the conversation information to their appropriate columns, then fetch the data with Pushbullets using the API key.

## Procedure to follow: 
```python
    pip install pandas
    pip install openpyxl
    pip install pushbullet.py == 0.9.1
```
- Authenticate the key now using **PushBullet**. If your key is invalid, an **InvalidKeyError** is thrown (the Pushbullet API returns 401).
- By using get pushes, you may retrieve all of your previous pushes, which includes all of the files you've sent to Pushbullet. However, we're interested in the most recent push, which will be at index '0' in a list of all pushes. We need to get the URL of our export chats from Pushbullet now that we've got the most recent push, so just pass the file URL.
- Create a text file to save all of the talks, and then get all of the data from the URL using the urlretrieve function. The URL and the text file in which to store all of the data are both accepted by urlretrieve.
- Using list slicing, create a loop to extract the date, time, name, and message from the file data. Once they've been extracted, just add them to a list.
- Finally, create a data frame using the Pandas library, which will be used to store all of the data on an Excel sheet. pd. A list of text and the columns to be produced on an excel sheet are the two inputs that DataFrame accepts. After that, just save them to an excel file using the excel function.

## Sample Output: 

![hey](https://github.com/Iamtripathisatyam/Awesome_Python_Scripts/blob/main/AutomationScripts/WhatsApp%20Backup%20to%20Excel/Images/Output.jpg)

