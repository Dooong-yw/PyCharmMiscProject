from backend.models.user_model import User

def analyze_data():
    users = User.query.all()
    # 示例：统计用户数量
    user_count = len(users)
    return {'user_count': user_count}