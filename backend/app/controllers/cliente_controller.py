from flask import request
from app.services.cliente_service import insertar_cliente

from flask import jsonify
from app.services.cliente_service import obtener_clientes

def get_clientes():

    clientes = obtener_clientes()

    data = []

    for cliente in clientes:
        data.append({
            "id_cliente": cliente[0],
            "nombre": cliente[1],
            "telefono": cliente[2],
            "correo": cliente[3]
        })

    return jsonify(data), 200


def create_cliente():

    data = request.get_json()

    if not data:
        return jsonify({
            "error": "Debe enviar datos JSON"
        }), 400

    nombre = data.get('nombre')
    telefono = data.get('telefono')
    correo = data.get('correo')
    cedula = data.get('cedula')

    if not nombre or not telefono or not correo or not cedula:

        return jsonify({
            "error": "Todos los campos son obligatorios"
        }), 400

    insertar_cliente(nombre, telefono, correo, cedula)

    return jsonify({
        "message": "Cliente creado correctamente"
    }), 201

def get_cliente(id_cliente):
    return jsonify({
        "message": f"Cliente {id_cliente}"
    })

def update_cliente(id_cliente):
    return jsonify({
        "message": f"Cliente {id_cliente} actualizado"
    })

def delete_cliente(id_cliente):
    return jsonify({
        "message": f"Cliente {id_cliente} eliminado"
    })