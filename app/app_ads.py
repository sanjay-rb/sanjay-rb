from app import app
from flask import render_template

@app.route("/app-ads.txt")
def app_ads():
    return render_template('app-ads.txt')