from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///market.db'     # configuring the database
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'               # entering the secret key
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)                                                # bcrypting the password
login_manager = LoginManager(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"
from market import routes
