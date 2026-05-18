from patterns.factory.producto_factory import ProductoFactory

from repositories.producto_repository import (
    ProductoRepository
)
from repositories.extra_repository import ExtraRepository
from models.extra import Extra


def crear_producto(
    nombre,
    categoria,
    precio,
    stock
):

    if precio <= 0:

        raise ValueError(
            "El precio debe ser mayor a 0"
        )

    producto = ProductoFactory.crear_producto(
        nombre,
        categoria,
        precio,
        stock
    )

    return ProductoRepository.crear(producto)


def obtener_productos():

    return ProductoRepository.obtener_todos()


def obtener_producto_por_id(producto_id):

    return ProductoRepository.obtener_por_id(
        producto_id
    )


def eliminar_producto(producto_id):

    return ProductoRepository.eliminar(
        producto_id
    )


def crear_extra(nombre, precio):

    extra = Extra(nombre=nombre, precio=precio)

    return ExtraRepository.crear(extra)


def obtener_extras():

    return ExtraRepository.obtener_todos()


def obtener_extra_por_id(extra_id):

    return ExtraRepository.obtener_por_id(extra_id)


def actualizar_extra(extra_id, nombre, precio):

    extra = ExtraRepository.obtener_por_id(extra_id)

    if extra:

        extra.nombre = nombre
        extra.precio = precio

        return ExtraRepository.actualizar(extra)

    return None


def eliminar_extra(extra_id):

    return ExtraRepository.eliminar(extra_id)