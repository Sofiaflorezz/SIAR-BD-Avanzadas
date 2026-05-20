CREATE TABLE producto (

    id_producto SERIAL PRIMARY KEY,

    nombre VARCHAR(100) NOT NULL,

    detalle_producto TEXT,

    precio NUMERIC(10,2) NOT NULL
    CHECK(precio > 0),

    stock INTEGER NOT NULL
    CHECK(stock >= 0)
);

CREATE TABLE ingrediente (

    id_ingrediente SERIAL PRIMARY KEY,

    detalle_ingrediente VARCHAR(100) NOT NULL,

    cantidad INTEGER NOT NULL
    CHECK(cantidad >= 0)
);

CREATE TABLE producto_ingrediente (

    id_producto INTEGER NOT NULL,

    id_ingrediente INTEGER NOT NULL,

    cantidad_usada INTEGER NOT NULL
    CHECK(cantidad_usada > 0),

    PRIMARY KEY(id_producto, id_ingrediente),

    FOREIGN KEY(id_producto)
    REFERENCES producto(id_producto),

    FOREIGN KEY(id_ingrediente)
    REFERENCES ingrediente(id_ingrediente)
);