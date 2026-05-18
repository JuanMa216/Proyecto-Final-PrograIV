from services.producto_service import crear_producto
from services.pedido_service import (
    crear_pedido,
    obtener_pedidos,
    cambiar_estado_pedido
)


producto = crear_producto(
    "Latte",
    "Bebida caliente",
    15000,
    10
)

pedido = crear_pedido([
    {
        "producto_id": producto.id,
        "cantidad": 2
    }
])

print(pedido)

pedidos = obtener_pedidos()

print(pedidos)

pedido_actualizado = cambiar_estado_pedido(
    pedido.id,
    "listo"
)

print(pedido_actualizado)