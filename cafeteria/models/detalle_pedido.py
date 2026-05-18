from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from database.conexion import Base


class DetallePedido(Base):
    __tablename__ = "detalle_pedido"

    id = Column(Integer, primary_key=True)
    pedido_id = Column(Integer, ForeignKey("pedidos.id"))
    producto_id = Column(Integer, ForeignKey("productos.id"))
    cantidad = Column(Integer, nullable=False)

    pedido = relationship("Pedido", back_populates="detalles")
    producto = relationship("Producto")