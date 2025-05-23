# 从flask包中导入Flask类

from flask import *
from flask_sqlalchemy import *
from sqlalchemy import *
from exts import db

# 使用Flask类创建app对象
app = Flask(__name__)


# __name__：模块或者包名称，这里是app.py模块名称
print("__name__", __name__)

# app.config[
#     'SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@localhost:3308/db_flask?charset=utf8'

app.config.from_object('config')
db.init_app(app)






with app.app_context():
    with db.engine.connect() as conn:
        rs = conn.execute(text("select 1"))
        print(rs.fetchone())

class graedmodel(db.Model):
    id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String(50))
    remark = db.Column(db.Text)#备注

with app.app_context(): # 根据模型建表
    db.create_all()

if __name__ == '__main__':
    app.run()
