from flask import Blueprint, render_template, request, redirect, url_for
from .forms import LogIn, SignUp

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    form = LogIn()
    if form.validate_on_submit():
        print(form.email.data, form.password.data)
        return redirect(url_for('views.hp', user_signed=True))
        
    return render_template('login.html', form=form, form_check=True)


@auth.route("logout")
def logout():
    return logout.__name__


@auth.route("sign-up", methods=['GET', 'POST'])
def signup():
    form = SignUp()
    if form.validate_on_submit():
        return redirect(url_for('views.hp', user_signed=True))
        
    return render_template('signup.html', form=form, form_check=True)

