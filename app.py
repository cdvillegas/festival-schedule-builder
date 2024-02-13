from flask import Flask
from routes.optimize_routes import optimize_bp

app = Flask(__name__)

# Register the Blueprint
app.register_blueprint(optimize_bp)

if __name__ == '__main__':
    app.run(debug=True)
