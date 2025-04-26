from flask import Blueprint, request, jsonify
from backend.services.data_integration_service import connect_to_iot_platform

# 创建蓝图
data_integration_bp = Blueprint('data_integration_bp', __name__)

# 连接物联中台
@data_integration_bp.route('/connect', methods=['POST'])
def connect():
    data = request.json
    try:
        result = connect_to_iot_platform(data['platform'], data['api_key'], data['params'])
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400