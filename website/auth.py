from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == 'POST':
        print("hello world")
    return render_template("admin-auth.html")


@auth.route("/user", methods=['GET', 'POST'])
def user():
    data = request.form
    print(data)
    return render_template("user-auth.html")


@auth.route("/superuser", methods=['GET', 'POST'])
def superuser():
    return render_template("super-auth.html")
