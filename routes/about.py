from flask import Blueprint, jsonify

about_bp = Blueprint('about', __name__)

@about_bp.route('/about')
def about():
    return jsonify({"message": "This is a generic Flask web server."})