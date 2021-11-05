import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

databse_uri = os.environ.get('DB_URL')
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = databse_uri

db = SQLAlchemy(app)

from app import home
from app import apps
from app import about
from app import contact
from app import app_ads
from app import get_app_info
from app import set_app_info
from app.razorpay_payment import payment