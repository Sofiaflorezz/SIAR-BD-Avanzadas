from flask import Blueprint
from app.controllers.cliente_controller import *

cliente_bp = Blueprint('cliente_bp', __name__)

cliente_bp.route('/clientes', methods=['GET'])(get_clientes)
cliente_bp.route('/clientes', methods=['POST'])(create_cliente)
cliente_bp.route('/clientes/<int:id_cliente>', methods=['GET'])(get_cliente)
cliente_bp.route('/clientes/<int:id_cliente>', methods=['PUT'])(update_cliente)
cliente_bp.route('/clientes/<int:id_cliente>', methods=['DELETE'])(delete_cliente)