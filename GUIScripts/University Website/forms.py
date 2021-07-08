from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, IntegerField
from wtforms.validators import Length, EqualTo, DataRequired, ValidationError
import application

class RegisterForm(FlaskForm):
    def validate_username(self, student_to_check):

        student = application.User.query.filter_by(username=student_to_check.data).first()
        if student:
            raise ValidationError('Username already exists! Please try a different username')

    def validate_email_address(self, email_address_to_check):
        email_address = application.User.query.filter_by(email_address=email_address_to_check.data).first()
        if email_address:
            raise ValidationError('Email Address already exists! Please try a different email address')

    roll_number = IntegerField(label='Roll Number:', validators=[DataRequired()])
    name = StringField(label='Name:', validators=[Length(min=2, max=50), DataRequired()])
    stream = StringField(label='Stream:', validators=[Length(min=1, max=50), DataRequired()])
    d_o_b = StringField(label='Date of Birth(DD/MM/YYYY):', validators=[Length(min=2, max=50), DataRequired()])
    email_address = StringField(label='Email Address:', validators=[DataRequired()])
    username = StringField(label='User Name:', validators=[Length(min=2, max=30), DataRequired()])
    password1 = PasswordField(label='Password:', validators=[Length(min=2), DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Create Account')


class LoginForm(FlaskForm):
    roll_number = IntegerField(label='Roll Number:', validators=[DataRequired()])
    username = StringField(label='User Name:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    submit = SubmitField(label='Sign in')


