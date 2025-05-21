from flask import Flask
from routes import home_bp, about_bp, hello_bp, echo_bp

app = Flask(__name__)

app.register_blueprint(home_bp)
app.register_blueprint(about_bp)
app.register_blueprint(hello_bp)
app.register_blueprint(echo_bp)

if __name__ == '__main__':
    app.run(debug=True)