from backend import db  # 从 __init__.py 中导入 db

class User(db.Model):
    __tablename__ = 'users'  # 数据库表名

    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(80), unique=True, nullable=False)  # 用户名，唯一且不能为空
    password = db.Column(db.String(120), nullable=False)  # 密码，不能为空
    role = db.Column(db.String(20), nullable=False)  # 用户角色：超级管理员、管理员、普通用户

    def __repr__(self):
        return f"<User(username='{self.username}', role='{self.role}')>"