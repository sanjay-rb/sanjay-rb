from flask import request, Response

from app import app, db
from app.model.appinfo import AppInfo

@app.route("/getinfo")
def getInfo():
    appid = request.args.get('appid')
    if appid:
        info = AppInfo.query.filter_by(appid=appid).first_or_404()
    else:
        return Response(status=404)
    return info.json()