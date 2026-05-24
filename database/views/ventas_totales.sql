-- Propósito: Vista financiera agregada por fechas para el control de caja diario.
-- Agrupa las facturas generadas mapeando la cronología de ingresos percibidos.

CREATE OR REPLACE VIEW ventas_totales AS

SELECT

    DATE(fecha_factura)
    AS fecha,

    SUM(total_precio)
    AS total_vendido

FROM factura

GROUP BY DATE(fecha_factura)

ORDER BY fecha DESC;