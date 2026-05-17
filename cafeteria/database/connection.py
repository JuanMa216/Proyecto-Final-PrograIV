# database/connection.py
# Patron: Singleton
#
# TODO: Clase DatabaseConnection
#   - TODO: Atributo privado _instancia (almacena la unica instancia)
#   - TODO: Atributo privado _conexion (almacena el objeto sqlite3.Connection)
#   - TODO: Metodo de clase get_instance() que retorne la instancia unica
#   - TODO: Metodo conectar() que abra conexion a SQLite y cree tablas
#   - TODO: Metodo desconectar() que cierre la conexion
#   - TODO: Metodo get_conexion() que retorne la conexion activa
#   - TODO: Metodo seed_admin() que inserte administrador por defecto
#   - TODO: Metodo _crear_tablas() con esquema de empleados, productos, pedidos, pedido_items
