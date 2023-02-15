from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

# Configure application
app = Flask(__name__)

# Use a secret token
app.config['SECRET_KEY'] = '6400945f04791b91638e31e1eb31491a'

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///side.db'
db = SQLAlchemy(app)

# Initialize the bcrypt password-hashing function
bcrypt = Bcrypt(app)

# Configure the Login Manager
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from app import routes
