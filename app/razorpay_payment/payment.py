from flask import request
from app import app, payment_client, api_key

@app.route("/payment")
def payment():
    amount = request.args.get('amount')
    payload = {
        "amount": float(amount) * 100.0,
        "currency": "INR",
    }
    result = payment_client.order.create(data=payload)
    result['key'] = api_key
    return result