from flask import Blueprint, render_template, request, redirect, url_for
from .forms import LogIn

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LogIn()
    if form.validate_on_submit():
        print(form.email.data, form.password.data)
        return redirect(url_for('views.hp'))
        
    return render_template('login.html', form=form)


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

