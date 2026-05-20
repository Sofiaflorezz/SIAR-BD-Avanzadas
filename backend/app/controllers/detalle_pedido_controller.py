from flask import request, jsonify

from app.services.detalle_pedido_service import (
    agregar_producto_pedido
)


def agregar_producto(id_pedido):

    data = request.json

    id_producto = data.get(
        "id_producto"
    )

    cantidad = data.get(
        "cantidad"
    )

    resultado = agregar_producto_pedido(
        id_pedido,
        id_producto,
        cantidad
    )

    if resultado == "producto_no_existe":

        return jsonify({
            "mensaje":
            "Producto no encontrado"
        }), 404


    if resultado == "stock_insuficiente":

        return jsonify({
            "mensaje":
            "Stock insuficiente"
        }), 400


    return jsonify({

        "mensaje":
        "Producto agregado",

        "subtotal":
        resultado

    }), 201