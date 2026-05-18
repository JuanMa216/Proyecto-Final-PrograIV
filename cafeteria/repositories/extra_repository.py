from database.conexion import get_session
from models.extra import Extra


class ExtraRepository:

    @staticmethod
    def crear(extra):
        session = get_session()
        session.add(extra)
        session.commit()
        session.refresh(extra)
        return extra

    @staticmethod
    def obtener_todos():
        session = get_session()
        return session.query(Extra).all()

    @staticmethod
    def obtener_por_id(extra_id):
        session = get_session()
        return session.query(Extra).filter_by(id=extra_id).first()

    @staticmethod
    def actualizar(extra):
        session = get_session()
        session.merge(extra)
        session.commit()
        return extra

    @staticmethod
    def eliminar(extra_id):
        session = get_session()
        extra = session.query(Extra).filter_by(id=extra_id).first()
        if extra:
            session.delete(extra)
            session.commit()
            return True
        return False
