CREATE TABLE pedido (

    id_pedido SERIAL PRIMARY KEY,

    id_cliente INTEGER NOT NULL,

    id_mesa INTEGER,

    fecha_pedido TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,

    estado VARCHAR(20)
    DEFAULT 'pendiente',

    total NUMERIC(10,2)
    CHECK(total >= 0),

    FOREIGN KEY(id_cliente)
    REFERENCES cliente(id_cliente),

    FOREIGN KEY(id_mesa)
    REFERENCES mesa(id_mesa)
);

CREATE TABLE detalle_pedido (

    id_detalle SERIAL PRIMARY KEY,

    id_pedido INTEGER NOT NULL,

    id_producto INTEGER NOT NULL,

    cantidad INTEGER NOT NULL
    CHECK(cantidad > 0),

    precio_unitario NUMERIC(10,2) NOT NULL
    CHECK(precio_unitario >= 0),

    subtotal NUMERIC(10,2) NOT NULL
    CHECK(subtotal >= 0),

    FOREIGN KEY(id_pedido)
    REFERENCES pedido(id_pedido),

    FOREIGN KEY(id_producto)
    REFERENCES producto(id_producto)
);

CREATE TABLE factura (

    id_factura SERIAL PRIMARY KEY,

    id_pedido INTEGER UNIQUE NOT NULL,

    fecha_factura TIMESTAMP
    DEFAULT CURRENT_TIMESTAMP,

    total_precio NUMERIC(10,2) NOT NULL
    CHECK(total_precio >= 0),

    metodo_pago VARCHAR(50),

    FOREIGN KEY(id_pedido)
    REFERENCES pedido(id_pedido)
);

CREATE TABLE pedido_audit (

    id SERIAL PRIMARY KEY,

    operacion CHAR(1),

    usuario TEXT,

    ts TIMESTAMPTZ DEFAULT now(),

    dato_viejo JSONB,

    dato_nuevo JSONB,

    id_pedido INT
);