from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        data = request.form
        print(data)
    return render_template('login.html')


@auth.route("logout")
def logout():
    return logout.__name__


@auth.route("sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        print(request.form)
        email = request.form.get('inputemail')
        first_name = request.form.get('fname')
        password = request.form.get('password')
        password_repeat = request.form.get('confirm-password')
        if request.form.get('rememberme') == 'on':
            remember = True
    return render_template('signup.html')

