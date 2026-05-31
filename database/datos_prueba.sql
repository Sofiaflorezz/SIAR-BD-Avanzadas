-- ============================================================
-- SIAR — Datos de prueba
-- Ejecutar después de todos los scripts de creación (01 al 04)
-- ============================================================


-- ------------------------------------------------------------
-- CLIENTES
-- ------------------------------------------------------------

INSERT INTO cliente (nombre, numero_telefono, correo, cedula) VALUES
    ('Carlos Mendoza',    '3001234567', 'carlos.mendoza@mail.com',  '1020304050'),
    ('Laura Ríos',        '3119876543', 'laura.rios@mail.com',      '1122334455'),
    ('Andrés Castaño',    '3204567890', 'andres.castano@mail.com',  '9988776655'),
    ('Valentina Torres',  '3156789012', 'vale.torres@mail.com',     '5544332211'),
    ('Miguel Herrera',    '3003216549', 'miguel.herrera@mail.com',  '6677889900');


-- ------------------------------------------------------------
-- MESAS
-- ------------------------------------------------------------

INSERT INTO mesa (numero_mesa, cantidad_sillas, ubicacion, estado) VALUES
    (1,  4, 'Interior',  'Disponible'),
    (2,  2, 'Terraza',   'Disponible'),
    (3,  6, 'Interior',  'Ocupada'),
    (4,  4, 'Terraza',   'Reservada'),
    (5,  8, 'Salón VIP', 'Disponible'),
    (6,  2, 'Barra',     'Mantenimiento');


-- ------------------------------------------------------------
-- RESERVAS
-- ------------------------------------------------------------

INSERT INTO reserva (id_cliente, id_mesa, fecha_reserva, hora_reserva, estado) VALUES
    (1, 4, '2026-05-28', '19:00', 'Confirmada'),
    (2, 2, '2026-05-29', '12:30', 'Confirmada'),
    (3, 5, '2026-05-27', '20:00', 'Finalizada'),
    (4, 1, '2026-05-26', '13:00', 'Cancelada'),
    (5, 4, '2026-05-30', '21:00', 'Confirmada');


-- ------------------------------------------------------------
-- INGREDIENTES
-- ------------------------------------------------------------

INSERT INTO ingrediente (detalle_ingrediente, cantidad) VALUES
    ('Arroz blanco (kg)',     20),
    ('Frijoles (kg)',         15),
    ('Carne de res (kg)',     10),
    ('Pollo (kg)',            12),
    ('Papa (kg)',             18),
    ('Tomate (kg)',           8),
    ('Cebolla (kg)',          6),
    ('Aceite (lt)',           5),
    ('Sal (kg)',              3),
    ('Pan (unidades)',        50);


-- ------------------------------------------------------------
-- PRODUCTOS
-- ------------------------------------------------------------

INSERT INTO producto (nombre, detalle_producto, precio, stock) VALUES
    ('Bandeja paisa',       'Arroz, frijoles, carne molida, chicharrón, huevo, aguacate', 28000.00, 30),
    ('Sancocho de pollo',   'Sopa tradicional con pollo, papa, yuca y mazorca',           22000.00, 25),
    ('Churrasco',           'Carne de res a la plancha con papas fritas y ensalada',      35000.00, 20),
    ('Pollo asado',         'Medio pollo asado con arroz y ensalada',                     24000.00, 18),
    ('Cazuela de mariscos', 'Mariscos en salsa de coco con arroz',                        42000.00, 10),
    ('Limonada de coco',    'Bebida refrescante con limón y coco',                         8000.00, 40),
    ('Jugo natural',        'Jugos de temporada: mango, maracuyá, mora',                  6000.00, 50),
    ('Café americano',      'Café negro 250ml',                                            4500.00, 60),
    ('Brownie con helado',  'Brownie de chocolate tibio con bola de helado de vainilla',  12000.00, 15),
    ('Agua mineral',        'Botella 500ml',                                               3000.00, 5);


-- ------------------------------------------------------------
-- PRODUCTO_INGREDIENTE
-- ------------------------------------------------------------

INSERT INTO producto_ingrediente (id_producto, id_ingrediente, cantidad_usada) VALUES
    (1, 1, 1),  -- Bandeja: arroz
    (1, 2, 1),  -- Bandeja: frijoles
    (1, 3, 1),  -- Bandeja: carne
    (2, 4, 1),  -- Sancocho: pollo
    (2, 5, 1),  -- Sancocho: papa
    (3, 3, 1),  -- Churrasco: carne
    (3, 5, 1),  -- Churrasco: papa
    (4, 4, 1),  -- Pollo asado: pollo
    (4, 1, 1);  -- Pollo asado: arroz


-- ------------------------------------------------------------
-- PEDIDOS
-- ------------------------------------------------------------

INSERT INTO pedido (id_cliente, id_mesa, estado, total) VALUES
    (1, 3, 'pendiente', 0),
    (2, 2, 'pendiente', 0),
    (3, 1, 'cerrado',   0),
    (4, 5, 'cerrado',   0),
    (5, 3, 'pendiente', 0);


-- ------------------------------------------------------------
-- DETALLE_PEDIDO
-- (precio_unitario se copia del producto al momento del pedido)
-- ------------------------------------------------------------

INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario, subtotal) VALUES
    (1, 1, 2, 28000.00, 56000.00),  -- Pedido 1: 2 bandejas
    (1, 6, 2,  8000.00, 16000.00),  -- Pedido 1: 2 limonadas
    (2, 3, 1, 35000.00, 35000.00),  -- Pedido 2: 1 churrasco
    (2, 8, 2,  4500.00,  9000.00),  -- Pedido 2: 2 cafés
    (3, 2, 3, 22000.00, 66000.00),  -- Pedido 3: 3 sancochos
    (3, 7, 3,  6000.00, 18000.00),  -- Pedido 3: 3 jugos
    (4, 4, 2, 24000.00, 48000.00),  -- Pedido 4: 2 pollos
    (4, 9, 2, 12000.00, 24000.00),  -- Pedido 4: 2 brownies
    (5, 5, 1, 42000.00, 42000.00),  -- Pedido 5: 1 cazuela
    (5, 6, 1,  8000.00,  8000.00);  -- Pedido 5: 1 limonada


-- ------------------------------------------------------------
-- ACTUALIZAR TOTALES DE PEDIDOS
-- ------------------------------------------------------------

UPDATE pedido SET total = (
    SELECT COALESCE(SUM(subtotal), 0)
    FROM detalle_pedido
    WHERE detalle_pedido.id_pedido = pedido.id_pedido
);


-- ------------------------------------------------------------
-- FACTURAS (solo pedidos cerrados)
-- ------------------------------------------------------------

INSERT INTO factura (id_pedido, total_precio, metodo_pago) VALUES
    (3, 84000.00, 'efectivo'),
    (4, 72000.00, 'tarjeta');