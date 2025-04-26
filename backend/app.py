from backend import app, db
from flask_cors import CORS

# 启用跨域支持
CORS(app)

# 注册路由蓝图
from routes.user_routes import user_bp
from routes.data_integration_routes import data_integration_bp
from routes.data_analysis_routes import data_analysis_bp

app.register_blueprint(user_bp, url_prefix='/api/users')
app.register_blueprint(data_integration_bp, url_prefix='/api/data-integration')
app.register_blueprint(data_analysis_bp, url_prefix='/api/data-analysis')

if __name__ == '__main__':
    app.run(debug=True)