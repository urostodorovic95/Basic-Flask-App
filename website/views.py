from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)


@views.route('/', methods=['GET'])
def hp():
    return render_template('home.html')

