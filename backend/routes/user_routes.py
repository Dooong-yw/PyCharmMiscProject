from flask import Blueprint, request, jsonify
from backend.models.user_model import User
from backend import db

# 创建蓝图
user_bp = Blueprint('user_bp', __name__)

# 添加用户
@user_bp.route('/add', methods=['POST'])
def add_user():
    data = request.json
    new_user = User(
        username=data['username'],
        password=data['password'],
        role=data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User added successfully'}), 201

# 获取用户列表
@user_bp.route('/list', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([{'id': u.id, 'username': u.username, 'role': u.role} for u in users]), 200