# services/pedido_service.py
# Patron: N/A (Service)
#
# TODO: Clase PedidoService
#   - TODO: Constructor que reciba un PedidoRepository
#   - TODO: Metodo crear_pedido(productos, empleado) que:
#     - TODO: Cree el pedido con estado Pendiente
#     - TODO: Notifique al EventBus con evento "pedido_creado"
#   - TODO: Metodo cambiar_estado(id_pedido) que:
#     - TODO: Use el patron State para avanzar al siguiente estado
#     - TODO: Notifique al EventBus con evento "estado_cambiado"
#   - TODO: Metodo listar_pendientes() que retorne pedidos activos
#   - TODO: Metodo listar_historial() que retorne pedidos finalizados
#   - TODO: Metodo obtener_pedido(id) que retorne un pedido con sus items
