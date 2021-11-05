from flask import request, Response

from app import app, db
from app.model.appinfo import AppInfo

@app.route("/setinfo")
def setInfo():
    appid = request.args.get('appid')
    version = request.args.get('version')
    build_number = request.args.get('build_number')
    info = AppInfo()
    if appid and version and build_number:
        info = AppInfo.query.filter_by(appid=appid).first()
        if info:
            # Update
            info.version = version
            info.build_number = build_number
        else:
            # Add
            info = AppInfo()
            info.addAppInfo(appid, version, build_number)
            db.session.add(info)
        db.session.commit()
    else:
        return Response(status=404)
    return info.json()