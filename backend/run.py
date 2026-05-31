from flask import Flask, send_from_directory
from flask_cors import CORS

from app.routes.cliente_routes import cliente_bp
from app.routes.producto_routes import producto_bp
from app.routes.pedido_routes import pedido_bp
from app.routes.detalle_pedido_routes import detalle_bp
from app.routes.estadisticas_routes import estadisticas_bp
from app.routes.operaciones_routes import operaciones_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(cliente_bp)
app.register_blueprint(producto_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(detalle_bp)
app.register_blueprint(estadisticas_bp)
app.register_blueprint(operaciones_bp)

@app.route("/")
def home():

    return send_from_directory(".", "index.html")

if __name__ == "__main__":

    app.run(
        debug=True
    )