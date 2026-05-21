CREATE OR REPLACE VIEW ventas_totales AS

SELECT

    DATE(fecha_factura)
    AS fecha,

    SUM(total_precio)
    AS total_vendido

FROM factura

GROUP BY DATE(fecha_factura)

ORDER BY fecha DESC;