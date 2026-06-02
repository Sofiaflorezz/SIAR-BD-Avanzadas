from flask import Blueprint
from app.controllers.pedido_controller import (
    crear_pedido,
    obtener_pedido,
    obtener_pedidos,
    cerrar_y_facturar
)

pedido_bp = Blueprint(
    "pedido_bp",
    __name__
)

pedido_bp.route(
    "/pedidos",
    methods=["POST"]
)(crear_pedido)

pedido_bp.route(
    "/pedidos",
    methods=["GET"]
)(obtener_pedidos)

pedido_bp.route(
    "/pedidos/<int:id_pedido>",
    methods=["GET"]
)(obtener_pedido)

pedido_bp.route(
    "/pedidos/<int:id_pedido>/cerrar",
    methods=["PUT"]
)(cerrar_y_facturar)

pedido_bp.route(
    "/pedidos/<int:id_pedido>/facturar",
    methods=["POST"]
)(cerrar_y_facturar)
