from database.conexion import get_session
from models.pedido import Pedido


class PedidoRepository:

    @staticmethod
    def crear(pedido):

        session = get_session()

        session.add(pedido)
        session.commit()
        session.refresh(pedido)

        return pedido

    @staticmethod
    def obtener_todos():

        session = get_session()

        pedidos = session.query(Pedido).all()

        return pedidos

    @staticmethod
    def obtener_por_id(pedido_id):

        session = get_session()

        pedido = session.query(Pedido).filter_by(
            id=pedido_id
        ).first()

        return pedido