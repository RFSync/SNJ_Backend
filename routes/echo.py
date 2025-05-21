from flask import Blueprint, jsonify, request

echo_bp = Blueprint('echo', __name__)

@echo_bp.route('/echo', methods=['POST'])
def echo():
    data = request.get_json()
    return jsonify({"you_sent": data})