from flask import Blueprint, render_template, request, redirect, url_for
from .forms import LogIn, SignUp
from .models import User
from . import db

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
        new_user = User(
            username=form.first_name.data,
            email=form.email.data
        )
        db.session.add(new_user)
        db.session.commit()
        print(f"User {db.session.get(User, new_user.id)} Added!")
        return redirect(url_for('views.hp', user_signed=True))
        
    return render_template('signup.html', form=form, form_check=True)

