from flask import render_template, redirect, url_for, flash
from flask_login import current_user, login_user, logout_user, login_required
from forms import RegisterForm, LoginForm
import application

roll_number = 0


def route(app, db):
    @app.route('/')
    @app.route('/home')
    def home_page():
        return render_template('home.html')

    @app.route('/details')
    @login_required
    def details_page():
        global roll_number
        detail = application.Student.query.filter_by(id=roll_number).all()
        return render_template('details.html', detail=detail)

    @app.route('/attendance')
    @login_required
    def attendance_page():
        attend = application.Attendance.query.filter_by(roll=roll_number).all()
        return render_template('attendance.html', attend=attend)

    @app.route('/course')
    @login_required
    def course_page():
        course = application.Course.query.filter_by(roll=roll_number).all()
        return render_template('course.html', course=course)

    @app.route('/time_table')
    @login_required
    def ttpage():
        ttable = application.Timetable.query.filter_by(roll=roll_number).all()
        return render_template('time_table.html', ttable=ttable)

    @app.route('/result')
    @login_required
    def result_page():
        global roll_number
        results = application.Result.query.filter_by(roll_number=roll_number).all()
        return render_template('result.html', results=results)

    @app.route('/fees')
    @login_required
    def fees_page():
        global roll_number
        fees = application.Fees.query.filter_by(id=roll_number).all()
        return render_template('fees.html', fees=fees)

    @app.route('/register', methods=['GET', 'POST'])
    def register_page():
        form = RegisterForm()
        db.create_all()
        if form.validate_on_submit():
            student_to_create = application.Student(id=form.roll_number.data, name=form.name.data,
                                                    stream=form.stream.data, d_o_b=form.d_o_b.data,
                                                    email_address=form.email_address.data, username=form.username.data,
                                                    password=form.password1.data)
            db.session.add(student_to_create)
            db.session.commit()
            login_user(student_to_create)
            flash(f"Account created successfully! You are now logged in as {student_to_create.username}",
                  category='success')
            application.Student.authenticated = True
            global roll_number
            roll_number = student_to_create.id
            return redirect(url_for('details_page'))
        if form.errors != {}:  # If there are not errors from the validations
            for err_msg in form.errors.values():
                flash(f'There was an error with creating a user: {err_msg}', category='danger')

        return render_template('register.html', form=form)

    @app.route('/login', methods=['GET', 'POST'])
    def login_page():
        form = LoginForm()
        if form.validate_on_submit():
            attempted_user = application.Student.query.filter_by(username=form.username.data).first()
            if attempted_user and attempted_user.check_password_correction(
                    attempted_password=form.password.data
            ) and attempted_user.id == form.roll_number.data:
                attempted_user.authenticated = True
                login_user(attempted_user)
                global roll_number
                roll_number = attempted_user.id
                flash(f'Success! You are logged in as: {attempted_user.name}', category='success')
                return redirect(url_for('details_page'))
            else:
                flash('Username, password  or roll number does not match! Please try again', category='danger')

        return render_template('login.html', form=form)

    @app.route('/logout')
    def logout_page():
        user = current_user
        user.authenticated = False
        logout_user()
        flash("You have been logged out!", category='info')
        return redirect(url_for("home_page"))
