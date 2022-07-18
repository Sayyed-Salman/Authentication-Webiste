from flask import Blueprint, flash, redirect, render_template, request, url_for
from .models import Person
from werkzeug.security import generate_password_hash, check_password_hash
from . import db

auth = Blueprint('auth', __name__)


def validate_user_input(name, email, password):
    if name and email and password:
        user = Person.query.filter_by(name=name).first()
        errors = []
        if user:
            errors.append("User Exists")
            if user.email:
                errors.append("Email Exists")
                return errors
        else:
            return "OK"


@auth.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == 'POST':
        # Login
        if request.form.get('username'):
            username = request.form.get('username')
            password = request.form.get('password')

            u = Person.query.filter_by(name=username).first()
            if u:
                if check_password_hash(u.password, password):
                    flash("Login Successfull")
                    return redirect(url_for('views.login_home', username=username, tag="admin"))
                else:
                    flash("incorrect password")
            else:
                flash("User does not exist!")
            print("Login Form Submitted !")

        # Register
        if request.form.get('name'):
            tag = "admin"
            name = request.form.get('name')
            pass_ = request.form.get('pass')
            email = request.form.get('email')

            test = validate_user_input(name, email, pass_)
            if test == "OK":
                new_user = Person(tag=tag, name=name, email=email,
                                  password=generate_password_hash(pass_, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash("Account Created Succesfully", category="success")
                return redirect(url_for('views.login_home', username=name, tag=tag))
            else:
                long_msg = " "
                for msg in test:
                    long_msg.join(msg)
                flash(long_msg)
                flash("Something went wrong !")
            print("Registration Form submitted")

    return render_template("admin-auth.html")


@auth.route("/user", methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        if request.form.get('username'):
            username = request.form.get('username')
            password = request.form.get('password')
            print("Login Form Submitted !")
            u = Person.query.filter_by(name=username).first()
            if u:
                if check_password_hash(u.password, password):
                    flash("Login Successfull")
                    return redirect(url_for('views.login_home', username=username, tag="user"))
                else:
                    flash("incorrect password")
            else:
                flash("User does not exist!")
            print("Login Form Submitted !")

        if request.form.get('name'):
            tag = "user"
            name = request.form.get('name')
            pass_ = request.form.get('pass')
            email = request.form.get('email')
            print("Registration Form submitted")
            test = validate_user_input(name, email, pass_)
            if test == "OK":
                new_user = Person(tag=tag, name=name, email=email,
                                  password=generate_password_hash(pass_, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash("Account Created Succesfully", category="success")
                return redirect(url_for('views.login_home', username=name, tag=tag))
            else:
                long_msg = " "
                for msg in test:
                    long_msg.join(msg)
                flash(long_msg)
                flash("Something went wrong !")
            print("Registration Form submitted")

    return render_template("user-auth.html")


@auth.route("/superuser", methods=['GET', 'POST'])
def superuser():
    if request.method == 'POST':
        if request.form.get('username'):
            username = request.form.get('username')
            password = request.form.get('password')
            print("Login Form Submitted !")
            u = Person.query.filter_by(name=username).first()
            if u:
                if check_password_hash(u.password, password):
                    flash("Login Successfull")
                    return redirect(url_for('views.login_home', username=username, tag="superuser"))
                else:
                    flash("incorrect password")
            else:
                flash("User does not exist!")
            print("Login Form Submitted !")

        if request.form.get('name'):
            tag = "superuser"
            name = request.form.get('name')
            pass_ = request.form.get('pass')
            email = request.form.get('email')
            print("Registration Form submitted")
            test = validate_user_input(name, email, pass_)
            if test == "OK":
                new_user = Person(tag=tag, name=name, email=email,
                                  password=generate_password_hash(pass_, method='sha256'))
                db.session.add(new_user)
                db.session.commit()
                flash("Account Created Succesfully", category="success")
                return redirect(url_for('views.login_home', username=name, tag=tag))
            else:
                long_msg = " "
                for msg in test:
                    long_msg.join(msg)
                flash(long_msg)
                flash("Something went wrong !")
            print("Registration Form submitted")
    return render_template("super-auth.html")


@auth.route("/logout")
def logout():
    return render_template('logout.html')
