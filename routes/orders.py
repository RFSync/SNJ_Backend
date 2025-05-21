from flask import Blueprint, request, jsonify

orders_bp = Blueprint('orders', __name__)

@orders_bp.route('/create_order', methods=['POST'])
def order_creation():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No JSON payload received'}), 400
    
    # TODO: Make order object and add to database
    #  TODO: call automaktion for Human to see

    return jsonify({'message': 'Order creation received.', 'data': data}), 200

@orders_bp.route('/get_order/<order_id>', methods=['GET'])
def get_order(order_id):
    # TODO: Retrieve order details from the database using order_id
    return jsonify({'message': f'Retrieved order {order_id} (placeholder).'}), 200