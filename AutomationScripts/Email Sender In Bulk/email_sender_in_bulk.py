import csv
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


email_user = "abc@gmail.com" #enter your mail id
password = "pass" # enter the password of your mail
subject = "Email Validation"

#reading the email file
with open('email.csv','r')as csvfile:
    reader = csv.reader(csvfile)
    for line in reader:
        text = "hello "+line[1]+" your "+line[2]+ " plan has been activated"
       # print(text)
        email_send = line[0]
        msg= MIMEMultipart()
        msg['From'] = email_user
        msg['To'] = email_send
        msg['Subject']= subject
        msg.attach(MIMEText(text,"plain"))
        text = msg.as_string()

        #establishing the server
        server = smtplib.SMTP_SSL("smtp.gmail.com",465)
        server.login(email_user,password)
        server.sendmail(email_user,email_send,text)

        server.quit()