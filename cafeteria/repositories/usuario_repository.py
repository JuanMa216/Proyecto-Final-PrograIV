from database.conexion import get_session
from models.usuario import Usuario


class UsuarioRepository:

    @staticmethod
    def obtener_por_username(username):

        session = get_session()

        usuario = session.query(Usuario).filter_by(
            username=username
        ).first()

        return usuario

    @staticmethod
    def obtener_todos():

        session = get_session()

        usuarios = session.query(Usuario).all()

        return usuarios