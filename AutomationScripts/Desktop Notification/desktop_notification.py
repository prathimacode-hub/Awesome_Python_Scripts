import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            #setting the title
            title="ALERT!!!",
            #seeting the message
            message="Take a break! It has been an hour!",
            #time for which notification will be shown
            timeout=10
        )
        time.sleep(3600)
