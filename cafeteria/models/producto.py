from sqlalchemy import Column, Integer, String, Float
from database.conexion import Base


class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    categoria = Column(String(50), nullable=False)
    precio = Column(Float, nullable=False)
    stock = Column(Integer, default=0)

    def __repr__(self):
        return f"<Producto {self.nombre}>"