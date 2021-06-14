# importing yagmail and its packages
import yagmail
# initiating connection with SMTP server
yag = yagmail.SMTP("adityaamazonn1@gmail.com", "adityaamazonn1ispassword")
yag.send("adityaamazonn2@gmail.com","Sending HTML Email","<h1>This is a HTML Line</h1>")
print("\nEmail Send!!\n")