from app.services.cliente_service import existe_cliente
from app.services.cliente_service import eliminar_cliente
from app.services.cliente_service import actualizar_cliente
from app.services.cliente_service import obtener_cliente_por_id

from flask import request
from app.services.cliente_service import insertar_cliente

from flask import jsonify
from app.services.cliente_service import obtener_clientes

def get_clientes():

    try:

        clientes = obtener_clientes()

        data = []

        for cliente in clientes:

            data.append({
                "id_cliente": cliente[0],
                "nombre": cliente[1],
                "telefono": cliente[2],
                "correo": cliente[3]
            })

        return jsonify({
            "success": True,
            "data": data
        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

def create_cliente():

    try:

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
            "success": True,
            "message": "Cliente creado correctamente"
        }), 201

    except Exception as e:

        return jsonify({
            "error": str(e)
        }), 500

def get_cliente(id_cliente):

    try:

        cliente = obtener_cliente_por_id(id_cliente)

        if not cliente:

            return jsonify({
                "success": False,
                "error": "Cliente no encontrado"
            }), 404

        data = {
            "id_cliente": cliente[0],
            "nombre": cliente[1],
            "telefono": cliente[2],
            "correo": cliente[3]
        }

        return jsonify({
            "success": True,
            "data": data
        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500

def update_cliente(id_cliente):

    try:

        cliente = existe_cliente(id_cliente)

        if not cliente:

            return jsonify({
                "success": False,
                "error": "Cliente no encontrado"
            }), 404

        data = request.get_json()

        if not data:

            return jsonify({
                "success": False,
                "error": "Debe enviar datos JSON"
            }), 400

        nombre = data.get('nombre')
        telefono = data.get('telefono')
        correo = data.get('correo')
        cedula = data.get('cedula')

        if not nombre or not telefono or not correo or not cedula:

            return jsonify({
                "success": False,
                "error": "Todos los campos son obligatorios"
            }), 400

        actualizar_cliente(
            id_cliente,
            nombre,
            telefono,
            correo,
            cedula
        )

        return jsonify({
            "success": True,
            "message": "Cliente actualizado correctamente"
        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500
def delete_cliente(id_cliente):

    try:

        cliente = existe_cliente(id_cliente)

        if not cliente:

            return jsonify({
                "success": False,
                "error": "Cliente no encontrado"
            }), 404

        eliminar_cliente(id_cliente)

        return jsonify({
            "success": True,
            "message": "Cliente eliminado correctamente"
        }), 200

    except Exception as e:

        return jsonify({
            "success": False,
            "error": str(e)
        }), 500




