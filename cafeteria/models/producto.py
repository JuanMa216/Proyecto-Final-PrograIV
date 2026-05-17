# models/producto.py
# Patron: N/A (clase base de dominio)
#
# TODO: Clase Producto
#   - TODO: Atributos: id, nombre, precio_base, categoria, descripcion
#   - TODO: Metodo calcular_precio() que retorne el precio_base
#   - TODO: Metodo __str__() con representacion del producto
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass 
class Producto(ABC):
    _nombre: str
    _precio: float
    _categoria: str
    _descripcion: str
    _disponible: bool

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def descripcion(self):
        return self._descripcion

    @property 
    def disponible(self):
        return self._disponible

    @precio.setter
    def precio(self, nuevo):
        if nuevo < 0:
            raise ValueError("El precio no puede ser negativo")
        self._precio = nuevo

    @disponible.setter
    def disponible(self, valor: bool):
        self._disponible = valor

    @abstractmethod
    def preparar(self) -> str:
        pass

    def __str__(self):
        estado = "Disponible" if self._disponible else "No disponible"
        return f"{self._nombre} - ${self._precio:,.0f} ({estado})" 