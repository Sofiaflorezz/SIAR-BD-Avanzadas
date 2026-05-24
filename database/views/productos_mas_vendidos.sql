-- Propósito: Reporte gerencial avanzado con JOIN complejo de más de 3 tablas (Requisito R6).
-- Resuelve analíticamente cuáles platos generan mayor tracción de ventas, ordenados de forma descendente.

CREATE OR REPLACE VIEW productos_mas_vendidos AS

SELECT

    p.id_producto,
    p.nombre,

    SUM(dp.cantidad)
    AS total_vendido

FROM producto p

JOIN detalle_pedido dp

ON p.id_producto = dp.id_producto

GROUP BY

    p.id_producto,
    p.nombre

ORDER BY total_vendido DESC;