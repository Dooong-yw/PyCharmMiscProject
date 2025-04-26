import os

class Config:
    # MySQL 数据库连接配置
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://username:password@localhost/battery_management'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 禁用修改跟踪以提高性能

    # 密钥（用于会话加密等）
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'

    # 其他配置
    CORS_HEADERS = 'Content-Type'  # 允许跨域请求