from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mailman import Mail
from decouple import config

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

# Configure Email
app.config['MAIL_SERVER'] = 'smtp.hostinger.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = config('EMAIL_USER')
app.config['MAIL_PASSWORD'] = config('EMAIL_PASS')
mail = Mail(app)

from app import routes
