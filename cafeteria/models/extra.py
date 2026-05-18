from sqlalchemy import Column, Integer, String, Float
from database.conexion import Base


class Extra(Base):
    __tablename__ = "extras"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    precio = Column(Float, nullable=False)

    def __repr__(self):
        return f"<Extra {self.nombre}>"
