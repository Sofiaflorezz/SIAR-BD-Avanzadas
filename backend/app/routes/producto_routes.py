from flask import Blueprint

from app.controllers.producto_controller import (
    obtener_productos,
    obtener_producto,
    crear_producto,
    actualizar_producto,
    eliminar_producto
)

producto_bp = Blueprint("producto_bp", __name__)


# GET todos
producto_bp.route(
    "/productos",
    methods=["GET"]
)(obtener_productos)


# GET por ID
producto_bp.route(
    "/productos/<int:id_producto>",
    methods=["GET"]
)(obtener_producto)


# POST
producto_bp.route(
    "/productos",
    methods=["POST"]
)(crear_producto)


# PUT
producto_bp.route(
    "/productos/<int:id_producto>",
    methods=["PUT"]
)(actualizar_producto)


# DELETE
producto_bp.route(
    "/productos/<int:id_producto>",
    methods=["DELETE"]
)(eliminar_producto)