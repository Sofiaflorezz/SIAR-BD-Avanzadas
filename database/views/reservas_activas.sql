-- Propósito: Vista de control operativo para el personal de mesa.
-- Muestra de forma inmediata las reservas que se encuentran vigentes y aprobadas.

CREATE OR REPLACE VIEW reservas_activas AS

SELECT

    id_reserva,
    id_cliente,
    id_mesa,
    fecha_reserva,
    hora_reserva

FROM reserva

WHERE estado='Confirmada';