from flask import Blueprint, jsonify, request
from app.config.db import get_connection

operaciones_bp = Blueprint("operaciones_bp", __name__)

# ==========================================
# ENDPOINTS PARA GESTIÓN DE MESAS
# ==========================================
@operaciones_bp.route("/mesas", methods=["GET"])
def listar_mesas():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # CORRECCIÓN: Usamos 'cantidad_sillas' según tu esquema 02_cliente_mesa_reserva.sql
        cursor.execute("SELECT id_mesa, numero_mesa, cantidad_sillas, estado FROM mesa ORDER BY numero_mesa;")
        mesas = cursor.fetchall()
        cursor.close()
        conn.close()
        # Mapeamos 'cantidad_sillas' a 'capacidad' para que el index.html lo lea sin problemas
        data = [{"id_mesa": m[0], "numero_mesa": m[1], "capacidad": m[2], "estado": m[3]} for m in mesas]
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ==========================================
# ENDPOINTS PARA GESTIÓN DE RESERVAS
# ==========================================
@operaciones_bp.route("/reservas", methods=["GET"])
def listar_reservas():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT r.id_reserva, c.nombre, r.id_mesa, r.fecha_reserva, r.hora_reserva, r.estado 
            FROM reserva r
            JOIN cliente c ON r.id_cliente = c.id_cliente
            ORDER BY r.fecha_reserva DESC;
        """)
        reservas = cursor.fetchall()
        cursor.close()
        conn.close()
        data = [{
            "id_reserva": r[0], "cliente": r[1], "id_mesa": r[2],
            "fecha": str(r[3]), "hora": str(r[4]), "estado": r[5]
        } for r in reservas]
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ==========================================
# ENDPOINTS PARA GESTIÓN DE INGREDIENTES
# ==========================================
@operaciones_bp.route("/ingredientes", methods=["GET"])
def listar_ingredientes():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # CORRECCIÓN: Usamos 'detalle_ingrediente' y 'cantidad' según tu esquema 03_producto_inventario.sql
        cursor.execute("SELECT id_ingrediente, detalle_ingrediente, cantidad FROM ingrediente ORDER BY detalle_ingrediente;")
        ingredientes = cursor.fetchall()
        cursor.close()
        conn.close()
        # Mapeamos a los nombres de variables del frontend y asignamos "Unidades" por defecto
        data = [{"id_ingrediente": i[0], "nombre": i[1], "stock_disponible": i[2], "unidad_medida": "uds"} for i in ingredientes]
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ==========================================
# INGREDIENTES DE UN PRODUCTO (RECETAS)
# ==========================================
@operaciones_bp.route("/productos/<int:id_producto>/ingredientes", methods=["GET"])
def obtener_receta(id_producto):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        # CORRECCIÓN: Ajustado a 'cantidad_usada' y 'detalle_ingrediente'
        cursor.execute("""
            SELECT i.detalle_ingrediente, pi.cantidad_usada
            FROM producto_ingrediente pi
            JOIN ingrediente i ON pi.id_ingrediente = i.id_ingrediente
            WHERE pi.id_producto = %s;
        """, (id_producto,))
        receta = cursor.fetchall()
        cursor.close()
        conn.close()
        data = [{"ingrediente": r[0], "cantidad_requerida": float(r[1]), "unidad": "uds"} for r in receta]
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500
    
# ==========================================
# RUTAS POST PARA CREAR NUEVAS MESAS, RESERVAS E INGREDIENTES
# ==========================================
@operaciones_bp.route("/mesas", methods=["POST"])
def crear_mesa():
    datos = request.get_json()
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO mesa (numero_mesa, cantidad_sillas, estado) VALUES (%s, %s, %s) RETURNING id_mesa;",
            (datos["numero_mesa"], datos["capacidad"], datos.get("estado", "Disponible"))
        )
        id_mesa = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"success": True, "id_mesa": id_mesa}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@operaciones_bp.route("/reservas", methods=["POST"])
def crear_reserva():
    datos = request.get_json()
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO reserva (id_cliente, id_mesa, fecha_reserva, hora_reserva, estado) VALUES (%s, %s, %s, %s, %s) RETURNING id_reserva;",
            (datos["id_cliente"], datos["id_mesa"], datos["fecha"], datos["hora"], "Confirmada")
        )
        id_reserva = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"success": True, "id_reserva": id_reserva}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@operaciones_bp.route("/ingredientes", methods=["POST"])
def crear_ingrediente():
    datos = request.get_json()
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ingrediente (detalle_ingrediente, cantidad) VALUES (%s, %s) RETURNING id_ingrediente;",
            (datos["nombre"], datos["stock_disponible"])
        )
        id_ingrediente = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({"success": True, "id_ingrediente": id_ingrediente}), 201
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500