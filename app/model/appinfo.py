from app import db

class AppInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    appid = db.Column(db.String, nullable=False)
    version = db.Column(db.String, nullable=False)
    build_number = db.Column(db.String, nullable=False)

    def addAppInfo(self, appid, version, build_number):
        self.appid = appid
        self.version = version
        self.build_number = build_number

    def __init__(self):
        db.create_all()

    def json(self):
        return {
            "id": self.id,
            "appid":self.appid,
            "version":self.version,
            "build_number":self.build_number,
        }
        
    def __repr__(self):
            return f"AppInfo({self.id}, {self.appid}, {self.version}, {self.build_number})"