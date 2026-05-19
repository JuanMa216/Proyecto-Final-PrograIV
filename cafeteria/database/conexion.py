from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from database.config import DATABASE_URL


engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()


def get_session():
    return SessionLocal()


def init_db():
    from models.usuario import Usuario
    from models.producto import Producto
    from models.pedido import Pedido
    from models.detalle_pedido import DetallePedido
    from models.extra import Extra

    Base.metadata.create_all(bind=engine)