# database model
from datetime import datetime
from sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    # 时间戳
    # 如果传入的时间戳不是方法对象而是方法本身，那么在加载模块时这个函数就会被执行，时间戳的值就不正确
    timestamp = db.Column(db.DateTime, default=datetime.now, index=True)