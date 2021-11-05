from app import app, db
from app.model.appinfo import AppInfo
from flask import render_template

@app.route("/apps")
def apps():
    AppInfo()
    apps = AppInfo.query.order_by(AppInfo.id).all()
    return render_template('apps.html', apps=apps)