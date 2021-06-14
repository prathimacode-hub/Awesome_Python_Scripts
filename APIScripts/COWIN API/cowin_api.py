import requests
from termcolor import colored

# Function used for printing output in the terminal in different colors
def color(s,c='g'):
    if(c=='g'):
        return colored(s,"green")
    elif(c=='y'):
        return colored(s,"yellow")       
    elif(c=='c'):
        return colored(s,"cyan")    
    elif(c=='b'):
        return colored(s,"blue")    
    elif(c=='m'):
        return colored(s,"magenta")
    elif(c=='r'):
        return colored(s,"red")

print(color("COWIN API\n",'y'))
print("1.Get vaccination sessions by PINCODE for a specific date")
print("2.Get vaccination sessions by district for a specific date")
print("3.Get vaccination sessions by PINCODE for 7 days")
print("4.Get vaccination sessions by district for 7 days")
url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/"
    
#The user is prompted to Enter the input repeatedly until she/he enters the correct option 
while True:
    print(color("\nEnter your option: ",'c'),end=" ")
    opt = int(input())
    if(not(opt == 1 or opt == 2 or opt == 3 or opt == 4)):
        print(color("Check your option!",'r'))
        continue
    else:
        print(color("\nEnter DATE (in DD-MM-YY format): ",'c'),end=" ")
        date = input()
        if(opt == 1):
            print(color("\nEnter PINCODE: ",'c'),end=" ")
            pincode = input()
            url += "findByPin?pincode=" + pincode + "&date=" + date
        elif(opt == 2):
            print(color("\nEnter DISTRICT ID: ",'c'),end=" ")
            district = input()
            url += "findByDistrict?district_id=" + district + "&date=" + date
        elif(opt == 3):
            print(color("\nEnter PINCODE: ",'c'),end=" ")
            pincode = input()
            url += "calendarByPin?pincode=" + pincode + "&date=" + date
        elif(opt == 4):
            print(color("\nEnter DISTRICT ID: ",'c'),end=" ")
            district = input()
            url += "calendarByDistrict?district_id=" + district + "&date=" + date
        break
        
head = {
        "content-type": "application/json"
       }

#try except block for Exception Handling while performing an API Request
try:       
    #The API is requested for details of available vaccination sessions 
    response = requests.get(url,headers = head)
    data = response.json()
    if(not(response.ok)): #To check if the response was successful
        print(color("An Error occurred: " + data['error'],'r'))
        exit(0)
except Exception as e:
    print(e)
                
if(opt == 1 or opt == 2): 
    sessions = data['sessions']
    if(len(sessions)==0): # When no vaccination session details are obtained
        print(color("\nNO VACCINE SLOTS AVAILABLE !\n",'r'))
    else:    
        for i in sessions:
            session_details = "\n"
            session_details+= color("CENTER ID: ") + str(i['center_id']) + "\n"
            session_details+= color("CENTER NAME: ") + i['name'] + "\n"
            session_details+= color("ADDRESS: ") + i['address'] + "\n"
            session_details+= color("LOCATION: ") + i['block_name'] + ", " + i['district_name'] + ", " + i['state_name'] + "\n"
            session_details+= color("PINCODE: ") + str(i['pincode']) + "\n"
            session_details+= color("DATE: ") + i['date'] + "\n"
                
            if(i['available_capacity_dose1']>0 or i['available_capacity_dose2']>0): #The available capacity of vaccine dose 1 and dose 2 are checked
                session_details+= color("TIMINGS: ") + i['from'] + " to " + i['to'] + "\n"
                session_details+= color("VACCINE: ") + i['vaccine'] + "\n"
                session_details+= color("MINIMUM AGE LIMIT: ") + str(i['min_age_limit']) + "\n"
                
                if(i['fee_type']=="Free"):
                    session_details+= color("FEE TYPE: ") + "Free"+ "\n"
                else:
                    session_details+= color("FEE TYPE: ") + "Paid" + "\n"
                    session_details+= color("FEE : ") + str(i['fee']) + "\n"
                
                if(i['available_capacity_dose1']==0):
                    session_details+= color("DOSE 1: Unavailable" + "\n",'r')
                else:
                    session_details+= color("AVAILABLE CAPACITY OF DOSE 1: ") + str(i['available_capacity_dose1']) + "\n"
                
                if(i['available_capacity_dose2']==0):
                    session_details+= color("DOSE 2: Unavailable",'r') + "\n"
                else:
                    session_details+= color("AVAILABLE CAPACITY OF DOSE 2: ") + str(i['available_capacity_dose2']) + "\n" 
                
                slots = i['slots'] 
                session_details+= color("\nTIMING SLOTS: ")             
                print(session_details) #The vaccination session details are displayed to the user
                for j in slots:
                    print(j)

            else: #The condition when the available capacity of vaccine dose 1 and dose 2 are 0
                print(session_details) #The vaccination session details are displayed to the user
                print(color("NO VACCINE AVAILABLE !!!\n",'r'))

elif(opt == 3 or opt == 4):
    centers = data['centers']    
    if(len(centers)==0): # When no vaccination session details are obtained
        print(color("\nNO VACCINE SLOTS AVAILABLE !\n",'r'))
    else:    
        for i in centers:
            sessions = i['sessions']
            
            center_details = "\n"
            center_details+= color("CENTER ID: ") + str(i['center_id']) + "\n"
            center_details+= color("CENTER NAME: ") + i['name'] + "\n" 
            center_details+= color("ADDRESS: ") + i['address'] + "\n"
            center_details+= color("LOCATION: ") + i['block_name'] + " " + i['district_name'] + " " + i['state_name'] + "\n"
            center_details+= color("PINCODE: ") +i['pincode'] + "\n"
            print(center_details) #The vaccination center details are displayed to the user
            flag=0 #flag variable to check if vaccine is available
            for j in sessions:
                session_details = "\n"            
                if(j['available_capacity_dose1']>0 or j['available_capacity_dose2']>0): #The available capacity of vaccine dose 1 and dose 2 are checked
                    flag = 1
                    if(flag==1): session_details+= color("AVAILABLE SESSIONS",'g') + "\n\n"
                    session_details+= color("DATE: ") + j['date'] + "\n"
                    session_details+= color("TIMINGS: ") + i['from'] + " to " + i['to'] + "\n"
                    session_details+= color("VACCINE: ") + j['vaccine'] + "\n"
                    session_details+= color("MINIMUM AGE LIMIT: ") + str(j['min_age_limit']) + "\n"
                                    
                    if(i['fee_type']=="Free"):
                        session_details+= color("FEE TYPE: ") + "Free"+ "\n"
                    else:
                        session_details+= color("FEE TYPE: ") + "Paid" + "\n"
                        vaccine_fees = i['vaccine_fees']
                        for k in vaccine_fees:
                            if(k['vaccine']==j['vaccine']):
                                session_details+= color("FEE : ") + str(k['fee']) + "\n"               
                    
                    if(j['available_capacity_dose1']==0):
                        session_details+= color("DOSE 1: Unavailable",'r') + "\n"
                    else:
                        session_details+= color("AVAILABLE CAPACITY OF DOSE 1: ") + str(j['available_capacity_dose1']) + "\n"
                    
                    if(j['available_capacity_dose2']==0):
                        session_details+= color("DOSE 2: Unavailable",'r') + "\n"
                    else:
                        session_details+= color("AVAILABLE CAPACITY OF DOSE 2: ") + str(j['available_capacity_dose2']) + "\n" 
                    
                    slots = j['slots'] 
                    session_details+= color("\nTIMING SLOTS: ")
                    print(session_details)  #The vaccination session details are displayed to the user
                    for k in slots:
                        print(k)

            if(flag==0):
                print(color("NO VACCINE AVAILABLE !!!\n",'r'))