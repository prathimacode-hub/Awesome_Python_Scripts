import subprocess
import re

# Get all the Wi-Fi profiles (ssid)
out = subprocess.check_output("netsh wlan show profiles").decode()

# Filter out only profile names from the output
matches = re.findall(r"(All User Profile)(.*)", out)

# List comprehension to remove any \n \r \t and spaces
profiles = [str(match[1]).split(":")[1].strip() for match in matches]


# File object to store passwords with ssid
with open("passwords.txt", "w+") as f:

    # Traversing each profile
    for profile in profiles:
        # try/except block to keep the script from crashing if there was an error while execution
        try:
            # Get password using key=clear flag
            get_pass = subprocess.check_output(
                f'netsh wlan show profile "{profile}" key=clear'
            ).decode()

            # Filter out the Password line from the output
            pass_by_profile = re.search(r"(Key Content)(.*)", get_pass)

            # Check if the password is present or wi-fi was open
            if pass_by_profile:
                password = pass_by_profile.group().split(":")[1].strip()
            else:
                password = "THE WIFI IS OPEN"

            # Write the profile name and password to the text file
            f.write(f"{profile} : {password}\n")
        except Exception:
            continue
