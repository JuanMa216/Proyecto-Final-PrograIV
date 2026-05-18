import hashlib

from repositories.usuario_repository import (
    UsuarioRepository
)


def hash_password(password):

    return hashlib.sha256(
        password.encode()
    ).hexdigest()


def login(username, password):

    usuario = UsuarioRepository.obtener_por_username(
        username
    )

    if usuario and usuario.password == hash_password(password):
        return usuario

    return None