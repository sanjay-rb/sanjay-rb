from flask import request
from app import app, payment_client

@app.route("/verify", methods=['POST'])
def verify():
    if request.method.lower() == 'post':
        try:
            params_dict = request.get_json()
            return payment_client.utility.verify_payment_signature(params_dict)
        except Exception as e:
            return {
                'isVerified' : False
            }