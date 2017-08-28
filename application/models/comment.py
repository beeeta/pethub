from . import db
from datetime import datetime

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    rescue_id = db.Column(db.Integer)
    index = db.Column(db.Integer)
    content = db.Colunm(db.String(500))
    postTime = db.Column(db.String(32))

    def __init__(self,rescue_id,index,content,postTime=None):
        self.rescue_id = rescue_id
        self.index = index
        self.content = content
        if postTime:
            postTime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')






