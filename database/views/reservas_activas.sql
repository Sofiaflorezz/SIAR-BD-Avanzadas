CREATE OR REPLACE VIEW reservas_activas AS

SELECT

    id_reserva,
    id_cliente,
    id_mesa,
    fecha_reserva,
    hora_reserva

FROM reserva

WHERE estado='Confirmada';