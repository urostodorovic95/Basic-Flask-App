from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()


def create_app():
    """Create a Flask app.
    Return the app object."""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.getenv('APP_KEY')  # generate with secrets.token_hex(16)
    return app

