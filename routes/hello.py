from flask import Blueprint, jsonify

hello_bp = Blueprint('hello', __name__)

@hello_bp.route('/hello/<name>')
def hello(name):
    return jsonify({"greeting": f"Hello, {name}!"})