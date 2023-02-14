from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configure application
app = Flask(__name__)

# Use a secret token
app.config['SECRET_KEY'] = '6400945f04791b91638e31e1eb31491a'

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///side.db'
db = SQLAlchemy(app)

from app import routes