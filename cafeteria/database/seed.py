from database.conexion import get_session

from models.usuario import Usuario
from models.producto import Producto
from models.extra import Extra

from services.auth_service import hash_password


def seed_data():

    session = get_session()

    admin_existente = session.query(Usuario).filter_by(
        username="admin"
    ).first()

    if not admin_existente:

        admin = Usuario(
            nombre="Administrador",
            username="admin",
            password=hash_password("admin123"),
            rol="admin"
        )

        cajero = Usuario(
            nombre="Laura",
            username="cajero01",
            password=hash_password("1234"),
            rol="cajero"
        )

        barista = Usuario(
            nombre="Carlos",
            username="barista01",
            password=hash_password("1234"),
            rol="barista"
        )

        session.add(admin)
        session.add(cajero)
        session.add(barista)

    productos_existentes = session.query(Producto).all()

    if not productos_existentes:

        productos = [

            Producto(
                nombre="Espresso",
                categoria="Bebida caliente",
                precio=3500,
                stock=50
            ),

            Producto(
                nombre="Americano",
                categoria="Bebida caliente",
                precio=4000,
                stock=50
            ),

            Producto(
                nombre="Latte",
                categoria="Bebida caliente",
                precio=5000,
                stock=50
            ),

            Producto(
                nombre="Capuccino",
                categoria="Bebida caliente",
                precio=5500,
                stock=50
            ),

            Producto(
                nombre="Mocha",
                categoria="Bebida caliente",
                precio=6000,
                stock=50
            ),

            Producto(
                nombre="Croissant",
                categoria="Snack",
                precio=4500,
                stock=30
            )
        ]

        session.add_all(productos)

    extras_existentes = session.query(Extra).all()

    if not extras_existentes:

        extras = [

            Extra(nombre="Azúcar", precio=500),
            Extra(nombre="Chantilly", precio=1000),
            Extra(nombre="Leche deslactosada", precio=800),
            Extra(nombre="Chocolate extra", precio=1200),
            Extra(nombre="Shot espresso extra", precio=1500),
            Extra(nombre="Canela", precio=300),
            Extra(nombre="Jarabe de vainilla", precio=700),
            Extra(nombre="Crema batida", precio=900),
        ]

        session.add_all(extras)

    session.commit()