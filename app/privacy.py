from app import app
from flask import render_template

@app.route("/privacy")
def privacy():
    return render_template('privacy.html')