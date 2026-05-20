-- Índice para búsquedas por cédula

CREATE INDEX idx_cliente_cedula
ON cliente(cedula);

-- Índice para búsquedas de productos

CREATE INDEX idx_producto_nombre
ON producto(nombre);

-- Índice para pedidos por fecha

CREATE INDEX idx_pedido_fecha
ON pedido(fecha_pedido);

-- Índice para reservas por fecha

CREATE INDEX idx_reserva_fecha
ON reserva(fecha_reserva);