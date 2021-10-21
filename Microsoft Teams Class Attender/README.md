# Microsoft Teams Online Class Attender

## Aim

This bot attends the online classes (or meetings) held on Microsoft teams, according to the given timetable.



## Purpose

Here's what I want my bot to do. It must join my classes on time, according to my timetable, and also leave the class as soon as it ends. It must also notify me whenever it joins a class, or leaves a class.


## Short description of package/script
- Selenium
- Time
- SQLITE3
- Schedule
- Datetime



## Workflow of the Project

My online classes are held on Microsoft Teams, so I'm going to use Selenium to create my bot. Now, selenium is a famous framework for automating and testing web applications, and it is available for many languages, including Python, which is my favorite.
I can now just give the bot, my Microsoft teams login credentials, my discord webhook URL, and my timetable. The bot will take care of the rest. Now I need not worry about missing my online classes.


## Setup instructions

There are few things you need to configure before running this bot.

 - Open Microsoft teams on your browser, login to your account, change the dashboard view to list view (from grid view), so that your classes are displayed in a list view. 
 - ![This is how list view looks like](https://i.imgur.com/SSDo8c6.png)
 - Open *bot.py*, and put your microsoft teams credentials in the **CREDS** dictionary. 
 - Example - `CREDS  = {'email' : 'myemail@email.com', 'passwd':'''mypassword'''}`
 - Open *discord_webhook.py* and put your discord webhook URL in the **webhook_url** variable. 
 - Example - `webhook_url = "https://discordapp.com/...."`
 - Make sure that the timezone of the PC is correct. If you're running the bot on cloud, you may want to manually change the timezone of the virtual machine to an appropriate time zone (i.e., the timezone that your online classes follow)



## Compilation Steps

- Clone the repository 
- Install requirements.txt `pip install -r requirements.txt`
- Run the bot `python microsoft-teams_bot.py`


## Output





## Author

- Rishav Kumar


