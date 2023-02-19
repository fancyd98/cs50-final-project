import os
from dotenv import load_dotenv

BASEDIR = os.path.abspath(os.path.dirname(__file__))

load_dotenv(os.path.join(BASEDIR, '.env'))

class Config:
    # Use a secret token
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")

    # Configure Email
    MAIL_SERVER = 'sandbox.smtp.mailtrap.io'
    MAIL_PORT = 2525
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.getenv("EMAIL_USER")
    MAIL_PASSWORD = os.getenv("EMAIL_PASS")
