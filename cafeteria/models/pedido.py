from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database.conexion import Base

class Pedido(Base):
    __tablename__ = "pedidos"

    id = Column(Integer, primary_key=True)
    estado = Column(String(50), default="pendiente")
    total = Column(Float, default=0)

    detalles = relationship("DetallePedido", back_populates="pedido")

    def __repr__(self):
        return f"<Pedido {self.id}>"