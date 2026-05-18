from patterns.factory.producto_factory import ProductoFactory

from repositories.producto_repository import (
    ProductoRepository
)


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