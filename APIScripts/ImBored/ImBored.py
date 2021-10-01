import requests

URL  = 'https://www.boredapi.com/api/activity/'


def get_Idea():
    print("Wait! Let me Think ...\n")
    response = requests.get(URL)
    if response.status_code == 200:
        print('--------------------------------------------------')
        print("Type : ",response.json()['type'])
        print("Activity :",response.json()['activity'])
        if(response.json()['participants']>1):
            print('You might need help from {} of your friends to complete this !'.format(response.json()['participants']-1))
        print('--------------------------------------------------')
        return
    print("Ahh ! Sorry I could not think anything, My brain couldn't be accessed.")

print ("\n")
print ("Hello , I'm here to help you get out of the boredom !" )
print (" * Just type \"ImBored\" to see some intresting things you can do.")
print (" * Just press \"q\" to quit anytime you want.")
print ("\n")
flag = True
while(flag):
    bored = input()
    if bored == 'q':
        break
    elif bored == "ImBored":
        get_Idea()
        print ("\n")
        print("I hope this my get you out of boredom. If not feel free to try again! ")
        print ("\n")
    else:
        print("Oops! I think you got the wrong spelling! Try Again !")

