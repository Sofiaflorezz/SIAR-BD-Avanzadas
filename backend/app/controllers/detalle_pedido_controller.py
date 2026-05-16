from flask import request, jsonify

from app.services.detalle_pedido_service import (
    agregar_producto_pedido
)


def agregar_producto(id_pedido):

    data = request.get_json()

    id_producto = data.get("id_producto")
    cantidad = data.get("cantidad")


    subtotal = agregar_producto_pedido(
        id_pedido,
        id_producto,
        cantidad
    )


    if subtotal == "producto_no_existe":

        return jsonify({
            "success": False,
            "message": "Producto no existe"
        }), 404


    if subtotal == "stock_insuficiente":

        return jsonify({
            "success": False,
            "message": "Stock insuficiente"
        }), 400


    return jsonify({

        "success": True,
        "message": "Producto agregado al pedido",
        "subtotal": subtotal

    }), 201