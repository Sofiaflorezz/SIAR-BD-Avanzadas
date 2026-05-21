    -- Subconsulta 1 
SELECT *

FROM cliente

WHERE id_cliente = (

    SELECT id_cliente

    FROM pedido

    GROUP BY id_cliente

    ORDER BY COUNT(*) DESC

    LIMIT 1

);

    -- Subconsulta 2 
SELECT *

FROM producto

WHERE id_producto = (

    SELECT id_producto

    FROM detalle_pedido

    GROUP BY id_producto

    ORDER BY SUM(cantidad) DESC

    LIMIT 1

);

    -- Subconsulta 3
SELECT *

FROM pedido

WHERE total > (

    SELECT AVG(total)

    FROM pedido

);