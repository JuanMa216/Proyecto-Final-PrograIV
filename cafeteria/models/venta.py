from sqlalchemy import Column, Integer, Float
from database.conexion import Base


class Venta(Base):
    __tablename__ = "ventas"

    id = Column(Integer, primary_key=True)
    total = Column(Float, nullable=False)