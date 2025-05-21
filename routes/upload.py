from flask import Blueprint, request, jsonify
from PIL import Image
import os
import requests

upload_bp = Blueprint('upload', __name__)

def is_valid_image_file(file):
    """Check if file ends with .jpeg or .png and is 1024x1024."""
    filename = file.filename.lower()
    if not (filename.endswith('.jpeg') or filename.endswith('.png')):
        return False
    try:
        img = Image.open(file)
        width, height = img.size
        file.seek(0)  # Reset file pointer after reading
        return width == 1024 and height == 1024
    except Exception:
        file.seek(0)
        return False

def upload_to_ec2_bucket(file):
    """
    Placeholder: Upload the file to your EC2 bucket.
    Return a public link to the uploaded file.
    """
    # TODO: Implement actual upload logic to EC2 bucket
    # For now, return a placeholder link
    return f"https://your-ec2-bucket-url/{file.filename}"

def call_trellis_api(payload):
    """
    Placeholder: Call the Trellis API with the given payload.
    """
    # TODO: Replace with actual Trellis API endpoint and authentication
    trellis_url = "https://trellis.api/endpoint"
    response = requests.post(trellis_url, json=payload)
    return response.json()

@upload_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if not is_valid_image_file(file):
        return jsonify({'error': 'Invalid file. Must be a .jpeg or .png of size 1024x1024.'}), 400

    file_url = upload_to_ec2_bucket(file)

    return jsonify({'message': f'File {file.filename} uploaded successfully.', 'url': file_url}), 200

@upload_bp.route('/trellis_webhook', methods=['POST'])
def trellis_webhook():
    payload = request.get_json()
    if not payload:
        return jsonify({'error': 'No JSON payload received'}), 400

    response = call_trellis_api(payload)

    return jsonify({'received': response}), 200