from app import app
from flask import render_template

@app.route("/policy")
def policy():
    return render_template('policy.html')