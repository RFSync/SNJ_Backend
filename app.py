from flask import Flask
from routes import home_bp, upload_bp, orders_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(upload_bp)
app.register_blueprint(orders_bp)

if __name__ == '__main__':
    app.run(debug=True)