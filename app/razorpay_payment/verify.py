from flask import request
from app import app, api_secret
import hmac
import hashlib

@app.route("/verify", methods=['POST'])
def verify():
    if request.method.lower() == 'post':
        params_dict = request.get_json()
        data = params_dict['razorpay_order_id'] + "|" + params_dict['razorpay_payment_id']
        signature = hmac.new(
            api_secret.encode(),
            msg=data.encode(),
            digestmod=hashlib.sha256
        ).hexdigest().lower()
        if params_dict['razorpay_signature'] == signature:
            return { 'isVerified' : True }
        else:
            return { 'isVerified' : False } 