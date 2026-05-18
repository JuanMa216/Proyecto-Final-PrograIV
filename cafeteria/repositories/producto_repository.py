from database.conexion import get_session
from models.producto import Producto


class ProductoRepository:

    @staticmethod
    def crear(producto):

        session = get_session()

        session.add(producto)
        session.commit()
        session.refresh(producto)

        return producto

    @staticmethod
    def obtener_todos():

        session = get_session()

        productos = session.query(Producto).all()

        return productos

    @staticmethod
    def obtener_por_id(producto_id):

        session = get_session()

        producto = session.query(Producto).filter_by(
            id=producto_id
        ).first()

        return producto

    @staticmethod
    def eliminar(producto_id):

        session = get_session()

        producto = session.query(Producto).filter_by(
            id=producto_id
        ).first()

        if producto:

            session.delete(producto)
            session.commit()

            return True

        return False