# 在Python中，每一个有效的Python文件都是模块，每一个包含__init__.py文件的文件夹都被视作包
# __init__.py文件通常被称作构造文件，文件可以为空，也可以用来放置包的初始化代码，当包或包内的模块被导入时，构造文件将被自动执行

from flask import Flask
# 扩展Bootstrap-Flask内置了可以快速渲染Bootstrap样式HTML组件的宏，并提供了内置的Bootstrap资源
from flask_bootstrap import Bootstrap
# Moment.js是一个用于处理时间和日期的开源JS库，它可以对时间和日期进行各种方式的处理
# 它会根据用户电脑中的时区设置在客户端使用JS来渲染时间和日期，而且还提供了丰富的时间渲染格式支持
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy


# 在单脚本中创建程序实例时，我们传入__name__变量作为Flask类构造方法的import_name参数值，因为Flask通过这个值来确认程序路径
# 当用包组织代码时，为了确保其他扩展或测试框架获得正确的路径值，最好以硬编码的形式写出包名称作为程序名称
app = Flask('sayhello')
app.config.from_pyfile('settings.py')
app.jinja_env.trim_blocks = True # 删除jinja2语句后的第一个空行
app.jinja_env.lstrip_blocks = True # 删除jinja2语句所在行之前的空格和制表符（tab）

db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
moment = Moment(app)

from sayhello import views, errors, commands