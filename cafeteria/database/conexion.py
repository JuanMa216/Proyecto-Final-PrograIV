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
# database/connection.py
# Patrón: Singleton

import sqlite3
import os

class DatabaseConnection:
    _instancia = None
    _conexion = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia

    def conectar(self):
        if self._conexion is None:
            os.makedirs("data", exist_ok=True)
            self._conexion = sqlite3.connect("data/cafeteria.db")
            self._conexion.row_factory = sqlite3.Row
            print("Conexión a DB establecida")
        return self._conexion

    def desconectar(self):
        if self._conexion is not None:
            self._conexion.close()
            self._conexion = None
            print("Conexion cerrada")

    def get_conexion(self):
        if self._conexion is None:
            return self.conectar()
        return self._conexion