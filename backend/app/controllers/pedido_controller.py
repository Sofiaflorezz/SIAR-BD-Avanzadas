from flask import request, jsonify

from app.services.pedido_service import cerrar_pedido
from flask import jsonify

from app.services.pedido_service import cerrar_pedido, crear_factura

from app.services.pedido_service import (
    create_pedido,
    get_pedido_by_id,
    get_pedidos
)


# ======================
# CREAR PEDIDO
# ======================

def crear_pedido():

    data = request.get_json()

    id_cliente = data.get("id_cliente")
    id_mesa = data.get("id_mesa")


    if not id_cliente:

        return jsonify({

            "success": False,
            "message": "id_cliente obligatorio"

        }), 400


    pedido_id = create_pedido(
        id_cliente,
        id_mesa
    )


    return jsonify({

        "success": True,
        "message": "Pedido creado",
        "id_pedido": pedido_id

    }), 201


# ======================
# OBTENER PEDIDO POR ID
# ======================

def obtener_pedido(id_pedido):

    datos = get_pedido_by_id(
        id_pedido
    )


    if not datos:

        return jsonify({

            "success": False,
            "message": "Pedido no existe"

        }), 404


    productos = []


    for fila in datos:

        productos.append({

            "producto": fila[3],
            "cantidad": fila[4],
            "subtotal": float(fila[5])

        })


    return jsonify({

        "success": True,

        "id_pedido": datos[0][0],

        "id_cliente": datos[0][1],

        "total": float(datos[0][2]),

        "productos": productos

    })


# ======================
# OBTENER TODOS PEDIDOS
# ======================

def obtener_pedidos():

    pedidos = get_pedidos()

    lista = []


    for pedido in pedidos:

        lista.append({

            "id_pedido": pedido[0],
            "id_cliente": pedido[1],
            "total": float(pedido[2]),
            "estado": pedido[3]

        })


    return jsonify({

        "success": True,
        "pedidos": lista

    })

def cerrar_pedido_controller(id_pedido):

    total = cerrar_pedido(id_pedido)

    if not total:

        return jsonify({
            "success": False,
            "message": "Pedido no existe"
        }), 404

    return jsonify({
        "success": True,
        "message": "Pedido cerrado",
        "total": float(total)
    })

def cerrar_y_facturar(id_pedido):

    total = cerrar_pedido(id_pedido)

    if not total:

        return jsonify({
            "success": False,
            "message": "Pedido no existe"
        }), 404

    factura_id = crear_factura(id_pedido)

    return jsonify({
        "success": True,
        "message": "Pedido cerrado y facturado",
        "total": float(total),
        "factura_id": factura_id
    })