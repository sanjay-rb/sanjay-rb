import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import razorpay

# Flask app instance
app = Flask(__name__)

# SQLAlchemy instance
databse_uri = os.environ.get('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = databse_uri
db = SQLAlchemy(app)

# razorpay client
api_key = os.environ.get('PAYMENT_ID')
api_secret = os.environ.get('PAYMENT_SECRET')
payment_client = razorpay.Client(auth=(api_key, api_secret))

# Website pages....
from app import home
from app import apps
from app import about
from app import policy
from app import not_found

# app-ads.txt file 
from app import app_ads

# live application details endpoint
from app import get_app_info
from app import set_app_info

# razorpay payment getway
from app.razorpay_payment import payment
from app.razorpay_payment import verify