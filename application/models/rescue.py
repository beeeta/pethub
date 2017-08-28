from . import db
from datetime import datetime

class Rescue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    content = db.Column(db.String(2000))
    city = db.Column(db.String(32))
    postTime = db.Column(db.String(32))

    def __init__(self,user_id,content,city,postTime=None):
        self.user_id = user_id
        self.content = content
        self.city = city
        if postTime:
            postTime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')






