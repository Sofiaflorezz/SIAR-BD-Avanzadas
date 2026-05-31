-- ----------------------------------------------------------------------------
-- Subconsulta 1: Identificación del Cliente Más Frecuente (Fidelización)
-- PROPÓSITO: Obtener el registro completo del cliente con mayor cantidad de pedidos.
-- MECANISMO DE BD: Ejecuta una subconsulta interna no correlacionada sobre la tabla 'pedido', 
-- agrupando por ID de cliente, contando sus registros y ordenándolos de manera descendente. 
-- El operador '=' intercepta el ID singular devuelto por el 'LIMIT 1' para filtrar la tabla externa 'cliente'.
-- ----------------------------------------------------------------------------
SELECT *

FROM cliente

WHERE id_cliente = (

    SELECT id_cliente

    FROM pedido

    GROUP BY id_cliente

    ORDER BY COUNT(*) DESC

    LIMIT 1

);

-- ----------------------------------------------------------------------------
-- Subconsulta 2: Identificación del Producto Estrella (Popularidad de Menú)
-- PROPÓSITO: Extraer los detalles del producto que ha acumulado la mayor cantidad de unidades vendidas.
-- MECANISMO DE BD: La subconsulta interna evalúa la tabla intermedia 'detalle_pedido',
-- agrupa los registros por 'id_producto' y consolida el volumen total mediante la función agregada 'SUM(cantidad)'.
-- El resultado filtra la consulta externa apuntando al índice de la llave primaria de la tabla 'producto'.
-- ----------------------------------------------------------------------------
SELECT *

FROM producto

WHERE id_producto = (

    SELECT id_producto

    FROM detalle_pedido

    GROUP BY id_producto

    ORDER BY SUM(cantidad) DESC

    LIMIT 1

);

-- ----------------------------------------------------------------------------
-- Subconsulta 3: Reporte de Órdenes con Ticket Superior al Promedio (Auditoría Financiera)
-- PROPÓSITO: Listar los pedidos cuyo valor total supera el promedio histórico de ventas del establecimiento.
-- MECANISMO DE BD: Calcula dinámicamente un valor escalar único correspondiente al promedio general 
-- empleando 'AVG(total)' sobre la tabla 'pedido'. La consulta externa realiza un escaneo filtrado donde 
-- la columna 'total' sea estrictamente mayor que dicho umbral calculado en tiempo de ejecución.
-- ----------------------------------------------------------------------------
SELECT *

FROM pedido

WHERE total > (

    SELECT AVG(total)

    FROM pedido

);