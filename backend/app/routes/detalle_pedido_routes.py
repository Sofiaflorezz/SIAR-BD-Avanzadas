from flask import Blueprint

from app.controllers.detalle_pedido_controller import (
    agregar_producto
)

detalle_bp = Blueprint(
    "detalle_bp",
    __name__
)


detalle_bp.route(

    "/pedidos/<int:id_pedido>/productos",
    methods=["POST"]

)(agregar_producto)