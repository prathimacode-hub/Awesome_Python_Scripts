# importing yagmail and its packages
import yagmail
# initiating connection with SMTP server
yag = yagmail.SMTP("Sender@gmail.com", "SenderPassword")
yag.send("Reciever@gmail.com","Subject Of EMail","<h1>Contents Of Email</h1>")
print("\nEmail Send!!\n")
