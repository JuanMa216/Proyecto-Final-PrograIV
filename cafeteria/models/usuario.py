from sqlalchemy import Column, Integer, String
from database.conexion import Base


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    rol = Column(String(50), nullable=False)

    def __repr__(self):
        return f"<Usuario {self.username}>"