from flask import request, jsonify

from app.services.producto_service import (
    get_all_productos,
    get_producto_by_id,
    create_producto,
    update_producto,
    delete_producto
)


def obtener_productos():

    productos = get_all_productos()

    return jsonify({
        "success": True,
        "data": productos
    }), 200


def obtener_producto(id_producto):

    producto = get_producto_by_id(id_producto)

    if not producto:

        return jsonify({
            "success": False,
            "message": "Producto no encontrado"
        }), 404

    return jsonify({
        "success": True,
        "data": producto
    }), 200


def crear_producto():

    data = request.get_json()

    nombre = data.get("nombre")
    detalle_producto = data.get("detalle_producto")
    precio = data.get("precio")
    stock = data.get("stock")

    if not nombre:

        return jsonify({
            "success": False,
            "message": "Nombre obligatorio"
        }), 400


    producto_id = create_producto(
        nombre,
        detalle_producto,
        precio,
        stock
    )

    return jsonify({
        "success": True,
        "message": "Producto creado",
        "id_producto": producto_id
    }), 201


def actualizar_producto(id_producto):

    data = request.get_json()

    nombre = data.get("nombre")
    detalle_producto = data.get("detalle_producto")
    precio = data.get("precio")
    stock = data.get("stock")

    existe = get_producto_by_id(id_producto)

    if not existe:

        return jsonify({
            "success": False,
            "message": "Producto no encontrado"
        }), 404


    update_producto(
        id_producto,
        nombre,
        detalle_producto,
        precio,
        stock
    )

    return jsonify({
        "success": True,
        "message": "Producto actualizado"
    }), 200


def eliminar_producto(id_producto):

    existe = get_producto_by_id(id_producto)

    if not existe:

        return jsonify({
            "success": False,
            "message": "Producto no encontrado"
        }), 404


    delete_producto(id_producto)

    return jsonify({
        "success": True,
        "message": "Producto eliminado"
    }), 200