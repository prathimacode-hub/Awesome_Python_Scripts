# importing required modules
import pywhatkit

# asking user for input of number,message and time
phone_number = input(
    "Enter the number with country code eg.'+91**********' ,Don't Forget to add the country code with a \"+\" :"
)
message = input("PLease enter the message you want to send to the receiver : ")
time_in_hours = int(
    input('Enter the Hour in +12 format e.g : 4pm should be entered as 16: '))
time_in_minutes = int(input('Enter the Minutes : '))

# sending message
try:
    pywhatkit.sendwhatmsg(phone_number, message, time_in_hours, time_in_minutes)
    print("Message successfully sent!")
except:
    print("There is something wrong with the input parameters please check again")
