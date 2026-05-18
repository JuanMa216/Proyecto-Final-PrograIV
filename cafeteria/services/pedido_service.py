from sqlalchemy.orm import joinedload

from database.conexion import get_session

from models.pedido import Pedido
from models.detalle_pedido import DetallePedido
from models.producto import Producto

from patterns.decorator.extras import ProductoBase, ExtraDecorator


def calcular_precio_con_extras(producto, extras):

    base = ProductoBase(producto)

    for extra_data in extras:

        base = ExtraDecorator(base, extra_data["nombre"], extra_data["precio"])

    return base.costo()


def crear_pedido(productos):

    session = get_session()

    pedido = Pedido(
        estado="pendiente"
    )

    total = 0

    session.add(pedido)
    session.flush()

    for item in productos:

        producto = session.query(Producto).filter_by(
            id=item["producto_id"]
        ).first()

        if producto:

            extras = item.get("extras", [])

            precio_unitario = calcular_precio_con_extras(producto, extras)

            subtotal = precio_unitario * item["cantidad"]

            total += subtotal

            detalle = DetallePedido(
                pedido_id=pedido.id,
                producto_id=producto.id,
                cantidad=item["cantidad"],
                extras=extras
            )

            session.add(detalle)

    pedido.total = total

    session.commit()
    session.refresh(pedido)

    return pedido


def obtener_pedidos():

    session = get_session()

    pedidos = session.query(Pedido).options(
        joinedload(Pedido.detalles).joinedload(
            DetallePedido.producto
        )
    ).all()

    return pedidos


def cambiar_estado_pedido(pedido_id, estado):

    session = get_session()

    pedido = session.query(Pedido).filter_by(
        id=pedido_id
    ).first()

    if pedido:

        pedido.estado = estado

        session.commit()

        session.refresh(pedido)

    return pedido


def eliminar_pedido(pedido_id):

    session = get_session()

    pedido = session.query(Pedido).filter_by(
        id=pedido_id
    ).first()

    if pedido:

        detalles = session.query(
            DetallePedido
        ).filter_by(
            pedido_id=pedido.id
        ).all()

        for detalle in detalles:
            session.delete(detalle)

        session.delete(pedido)

        session.commit()

        return True

    return False