from flask import Blueprint, jsonify
from backend.services.data_analysis_service import analyze_data

# 创建蓝图
data_analysis_bp = Blueprint('data_analysis_bp', __name__)

# 分析数据
@data_analysis_bp.route('/analyze', methods=['GET'])
def analyze():
    result = analyze_data()
    return jsonify(result), 200