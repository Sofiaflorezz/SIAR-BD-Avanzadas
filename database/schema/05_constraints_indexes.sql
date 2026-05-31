-- Índice para búsquedas por cédula.

-- Se crea sobre la columna 'cedula' en la tabla 'cliente' debido a que es un campo con alta selectividad,
-- utilizado frecuentemente en las cláusulas WHERE para operaciones de autenticación, validación de registros únicos y búsquedas en el sistema.
CREATE INDEX idx_cliente_cedula
ON cliente(cedula);

-- Índice para búsquedas de productos

-- Se establece sobre la columna 'nombre' de la tabla 'producto'. Esto optimiza de forma drástica 
-- el tiempo de respuesta de las consultas ejecutadas por la API REST cuando el frontend solicita buscar productos por su nombre.
CREATE INDEX idx_producto_nombre
ON producto(nombre);

-- Índice para pedidos por fecha

-- Se crea sobre la columna 'fecha_pedido' en la tabla 'pedido' para mejorar el rendimiento de las consultas que filtran pedidos por fecha,
-- especialmente en reportes y análisis de ventas, donde es común agrupar o filtrar pedidos por rangos de fechas. Esto es crucial para la eficiencia 
-- de la API REST al manejar grandes volúmenes de datos históricos.   
CREATE INDEX idx_pedido_fecha
ON pedido(fecha_pedido);

-- Índice para reservas por fecha

-- Se establece sobre la columna 'fecha_reserva' en la tabla 'reserva' para optimizar las consultas que buscan reservas por fecha,
-- lo cual es común en la gestión de reservas y en la generación de reportes relacionados con la ocupación y la planificación de recursos.
-- Esto mejora significativamente el rendimiento de la API REST al manejar consultas relacionadas con reservas. 
CREATE INDEX idx_reserva_fecha
ON reserva(fecha_reserva);