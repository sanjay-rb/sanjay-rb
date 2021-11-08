from flask import request
from app import app
import hmac
import hashlib

@app.route("/verify", methods=['POST'])
def verify():
    if request.method.lower() == 'post':
        try:
            params_dict = request.get_json()
            print('params', params_dict)
            data = params_dict['razorpay_order_id'] + "|" + params_dict['razorpay_payment_id']
            signature = hmac.new(
                str(API_SECRET),
                msg=data,
                digestmod=hashlib.sha256
            ).hexdigest().lower()
            print(signature)
            print(params_dict['razorpay_signature'] == signature)
            if params_dict['razorpay_signature'] == signature:
                return { 'isVerified' : True }
            else:
                return { 'isVerified' : False }   
        except Exception as e:
            return { 'isVerified' : False }