from services.producto_service import (
    crear_producto,
    obtener_productos,
    obtener_producto_por_id,
    actualizar_stock
)


producto = crear_producto(
    "Capuccino",
    "Bebida caliente",
    12000,
    20
)

print(producto)

productos = obtener_productos()

print(productos)

producto_id = producto.id

producto_encontrado = obtener_producto_por_id(producto_id)

print(producto_encontrado)

producto_actualizado = actualizar_stock(producto_id, 50)

print(producto_actualizado)