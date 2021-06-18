import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
class email():
    def __init__(self):
        self.server=smtplib.SMTP_SSL(host="smtp.gmail.com",port=465)
        self.mssg = MIMEMultipart()
    def mail(self,to,sub,msg):
        
        try:
            self.server.login("email@gmail.com", "password")
            
            self.mssg['Subject']=sub
            self.mssg.attach(MIMEText(msg,'plain'))
            text=self.mssg.as_string()
            self.server.sendmail("example@gmail.com",to,text)
            self.server.quit()
            return "Email sent successfully to "
        except:
            return "Sorry, Could Not send the mail to "









