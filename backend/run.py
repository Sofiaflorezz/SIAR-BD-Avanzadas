from flask import Flask

from app.routes.cliente_routes import cliente_bp
from app.routes.producto_routes import producto_bp
from app.routes.pedido_routes import pedido_bp
from app.routes.detalle_pedido_routes import detalle_bp


app = Flask(__name__)


app.register_blueprint(cliente_bp)
app.register_blueprint(producto_bp)
app.register_blueprint(pedido_bp)
app.register_blueprint(detalle_bp)


@app.route("/")
def home():

    return {
        "message": "SIAR API funcionando"
    }


if __name__ == "__main__":

    app.run(
        debug=True
    )