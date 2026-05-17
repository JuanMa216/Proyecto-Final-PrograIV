# models/comida.py
# Patron: N/A (modelo de dominio)
#
# TODO: Clase Comida (hereda de Producto)
#   - TODO: Atributos: peso_gramos, ingredientes
#   - TODO: Propiedad con getter y setter para peso_gramos
#
# TODO: Clase Pasteleria (hereda de Comida)
#   - TODO: Constructor con atributos especificos de reposteria
#
# TODO: Clase Snack (hereda de Comida)
#   - TODO: Constructor con atributos especificos de snack
# models/comida.py
from dataclasses import dataclass
from models.producto import Producto


@dataclass
class Comida(Producto):
    _tiempo_preparacion: int 

    
    @property
    def tiempo_preparacion(self):
        return self._tiempo_preparacion

    
    @tiempo_preparacion.setter
    def tiempo_preparacion(self, valor: int):
        if valor < 0:
            raise ValueError("El tiempo de preparación no puede ser negativo")
        self._tiempo_preparacion = valor

    
    def preparar(self) -> str:
        return f"Preparando {self._nombre}, tiempo estimado: {self._tiempo_preparacion} min"

    def __str__(self):
        return (f"{self._nombre} | "
                f"{self._tiempo_preparacion} min | "
                f"${self._precio:,.0f}")


@dataclass
class Pasteleria(Comida):

    def preparar(self) -> str:
        return f"Horneando {self._nombre}, listo en {self._tiempo_preparacion} min..."


@dataclass
class Snack(Comida):

    def preparar(self) -> str:
        return f"Sirviendo {self._nombre}, listo en {self._tiempo_preparacion} min..."