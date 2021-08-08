# import required libraries
from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = 'hello123'

app.config['MAIL_SERVER'] = "smtp.gmail.com"
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'dreji1234@gmail.com'
app.config['MAIL_PASSWORD'] = 'Abc45678*'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

# routes of url
@app.route('/')
def home():
    flash("This is a flashed message.")
    return render_template('home.html')

# data given in the form comes here
@app.route('/send', methods=['POST','GET'])
def send():
    s= ""
    em = request.form['em']
    sub = request.form['sub']
    body = request.form['body']  
    s=em.split(",") 
    n=len(s)
    for i in range(0,n):
       
        msg = Message(sub, sender='dreji1234@gmail.com', recipients=[s[i]])
        msg.body = body
        mail.send(msg)
        i=i+1
    return render_template('home.html',msg=1)
        
        
         


if __name__ == '__main__':
	app.run(debug=True)
    
    

	
    


