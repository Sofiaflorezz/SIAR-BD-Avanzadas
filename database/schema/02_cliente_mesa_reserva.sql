CREATE TABLE cliente (

    id_cliente SERIAL PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    numero_telefono VARCHAR(20) NOT NULL,

    correo VARCHAR(100) UNIQUE,

    cedula VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE mesa (

    id_mesa SERIAL PRIMARY KEY,

    numero_mesa INTEGER UNIQUE NOT NULL,

    cantidad_sillas INTEGER NOT NULL
    CHECK(cantidad_sillas > 0),

    ubicacion VARCHAR(50),

    estado VARCHAR(20) NOT NULL
    CHECK(
        estado IN (
            'Disponible',
            'Reservada',
            'Ocupada',
            'Mantenimiento'
        )
    )
);

CREATE TABLE reserva (

    id_reserva SERIAL PRIMARY KEY,

    id_cliente INTEGER NOT NULL,

    id_mesa INTEGER NOT NULL,

    fecha_reserva DATE NOT NULL,

    hora_reserva TIME NOT NULL,

    estado VARCHAR(20) NOT NULL
    CHECK(
        estado IN (
            'Confirmada',
            'Cancelada',
            'Finalizada'
        )
    ),

    FOREIGN KEY(id_cliente)
    REFERENCES cliente(id_cliente),

    FOREIGN KEY(id_mesa)
    REFERENCES mesa(id_mesa)
);