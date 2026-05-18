from database.conexion import get_session
from models.venta import Venta


def registrar_venta(total):
    session = get_session()

    venta = Venta(total=total)

    session.add(venta)
    session.commit()
    session.refresh(venta)

    return venta


def obtener_ventas():
    session = get_session()

    ventas = session.query(Venta).all()

    return ventas