from flask import Flask
from app.routes.cliente_routes import cliente_bp

app = Flask(__name__)

app.register_blueprint(cliente_bp)

@app.route('/')
def home():
    return {
        "message": "SIAR API funcionando"
    }

if __name__ == '__main__':
    app.run(debug=True)