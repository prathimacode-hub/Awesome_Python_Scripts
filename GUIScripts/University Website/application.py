from flask import Flask
import routes
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///student.sqlite3'
app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = "login_page"
login_manager.login_message_category = "info"

# Data Base Classes


@login_manager.user_loader
def load_user(user_id):
    try:
        return Student.query.get(int(user_id))
    except:
        return None


class Student(db.Model, UserMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=50), nullable=False)
    stream = db.Column(db.String(length=50))
    d_o_b = db.Column(db.String(length=50))
    email_address = db.Column(db.String(length=50), nullable=False, unique=True)
    username = db.Column(db.String(length=30), nullable=False, unique=True)
    password_hash = db.Column(db.String(length=60), nullable=False)

    @property
    def password(self):
        return self.password

    @password.setter
    def password(self, plain_text_password):
        self.password_hash = bcrypt.generate_password_hash(plain_text_password).decode('utf-8')

    def check_password_correction(self, attempted_password):
        return bcrypt.check_password_hash(self.password_hash, attempted_password)

    def is_authenticated(self):
        return self.authenticated

    def is_active(self):
        return True

    def is_anonymous(self):
        return False


class Course(db.Model):
    roll = db.Column(db.Integer(), nullable=False)
    faculty_id = db.Column(db.Integer(), primary_key=True)
    faculty_name = db.Column(db.String(length=50), nullable=False)
    course_name = db.Column(db.String(length=50), nullable=False)
    faculty_email = db.Column(db.String(length=50), nullable=False)
    faculty_mobile = db.Column(db.String(length=12), nullable=False)

    def __repr__(self):
        return f'Fees {self.faculty_id}'


class Fees(db.Model):
    id = db.Column(db.Integer(), nullable=False, primary_key=True)
    name = db.Column(db.String(length=30), nullable=False)
    amount = db.Column(db.Integer(), nullable=False)
    fees_desc = db.Column(db.String(length=1024), nullable=False)

    def __repr__(self):
        return f'Fees {self.id}'


class Result(db.Model):
    roll_number = db.Column(db.Integer(), nullable=False, primary_key=True)
    course_name = db.Column(db.String(length=30), primary_key=True)
    grade = db.Column(db.String(length=5), nullable=False)
    sgpa = db.Column(db.String(length=5), nullable=False)

    def __repr__(self):
        return f'Result {self.course_name}'


class Attendance(db.Model):
    roll = db.Column(db.Integer(), nullable=False)
    course = db.Column(db.String(length=50), nullable=False, primary_key=True)
    total_days = db.Column(db.Integer(), nullable=False)
    present_days = db.Column(db.Integer(), nullable=False)
    absent_days = db.Column(db.Integer(), nullable=False)
    percentage = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f'Result {self.total_days}'


class Timetable(db.Model):
    roll = db.Column(db.Integer(), nullable=False)
    course1 = db.Column(db.String(length=50), nullable=False,primary_key=True)
    course2 = db.Column(db.String(length=50), nullable=False)
    course3 = db.Column(db.String(length=50), nullable=False)
    course4 = db.Column(db.String(length=50), nullable=False)
    course5 = db.Column(db.String(length=50), nullable=False)
    course6 = db.Column(db.String(length=50), nullable=False)
    days = db.Column(db.String(length=50), nullable=False)

# Routes


routes.route(app, db)

