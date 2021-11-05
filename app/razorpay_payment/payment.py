from flask import request
from app import app
import razorpay, os

@app.route("/payment")
def payment():
    api_key = os.environ.get('PAYMENT_ID')
    api_secret = os.environ.get('PAYMENT_SECRET')
    client = razorpay.Client(auth=(api_key, api_secret))
    amount = request.args.get('amount')
    payload = {
        "amount": float(amount) * 100.0,
        "currency": "INR",
    }
    result = client.order.create(data=payload)
    result['key'] = api_key
    return result