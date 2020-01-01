# database model
from datetime import datetime
from sayhello import db

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(200))
    name = db.Column(db.String(20))
    # 时间戳
    # 如果传入的时间戳不是方法对象而是方法本身，那么在加载模块时这个函数就会被执行，时间戳的值就不正确
    # 为了让不同时区的用户能看到自己的时间，一个简单的方法时通过JS在用户自己的浏览器进行时间转换
    # 为了能够在不同时区的客户端进行时间转换，需要在服务器端提供纯正的时间(naive time)，即不包含时区信息的时间戳
    # 与之相对，包含时区的时间戳被称为细致的时间(aware time)
    # datetime.utcnow()方法用来生成当前的UTC纯正时间
    timestamp = db.Column(db.DateTime, default=datetime.utcnow, index=True)