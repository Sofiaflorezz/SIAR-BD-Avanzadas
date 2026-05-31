from flask import Blueprint, jsonify
from app.config.db import get_connection

estadisticas_bp = Blueprint("estadisticas_bp", __name__)

@estadisticas_bp.route("/estadisticas/mejor-cliente", methods=["GET"])
def get_mejor_cliente():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT nombre, correo FROM cliente
            WHERE id_cliente = (
                SELECT id_cliente FROM pedido
                GROUP BY id_cliente ORDER BY COUNT(*) DESC LIMIT 1
            );
        """)
        cliente = cursor.fetchone()
        conn.close()
        if cliente:
            return jsonify({"success": True, "nombre": cliente[0], "correo": cliente[1]}), 200
        return jsonify({"success": False}), 404
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@estadisticas_bp.route("/estadisticas/top-productos", methods=["GET"])
def get_top_productos():
    # Cumple Requisito R6: Vista Compleja
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT nombre, total_vendido FROM productos_mas_vendidos LIMIT 5;")
        productos = cursor.fetchall()
        conn.close()
        
        data = [{"nombre": p[0], "total_vendido": p[1]} for p in productos]
        return jsonify({"success": True, "data": data}), 200
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500