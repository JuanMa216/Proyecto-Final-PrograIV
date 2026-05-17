# models/bebida.py
# Patron: N/A (modelo de dominio)
#
# TODO: Clase Bebida (hereda de Producto)
#   - TODO: Atributos: tamanio (pequeno, mediano, grande), personalizaciones, temperatura
#   - TODO: Propiedades con getters y setters para tamanio y temperatura
#   - TODO: Sobrescribir calcular_precio() para ajustar segun tamanio
#
# TODO: Clase BebidaCaliente (hereda de Bebida)
#   - TODO: Constructor que fije temperatura como "Caliente"
#
# TODO: Clase BebidaFria (hereda de Bebida)
#   - TODO: Constructor que fije temperatura como "Fria"
from dataclasses import dataclass
from enum import Enum
from models.producto import Producto

class Temperatura(Enum):
    CALIENTE = "Caliente"
    FRIA = "Fria"

class Tamaño(Enum):
    PEQUEÑO = "Pequeño"
    MEDIANO = "Mediano"
    GRANDE = "Grande"

@dataclass
class Bebida(Producto):
    _temperatura: Temperatura
    _tamaño: Tamaño

    #getters
    @property
    def temperatura(self):
        return self._temperatura

    @property
    def tamaño(self):
        return self._tamaño

    #setters
    @temperatura.setter
    def temperatura(self, valor: Temperatura):
        if not isinstance(valor, Temperatura):
            raise ValueError("Temperatura invalida, use Temperatura.CALIENTE o Temperatura.FRIA")
        self._temperatura = valor

    @tamaño.setter
    def tamaño(self, valor: Tamaño):
        if not isinstance(valor, Tamaño):
            raise ValueError("Tamaño invalido, use Tamaño.PEQUEÑO, MEDIANO o GRANDE")
        self._tamaño = valor

    def preparar(self) -> str:
        return (f"Preparando {self._nombre} "
                f"{self._temperatura.value} "
                f"tamaño {self._tamaño.value}")

    def __str__(self):
        return (f"{self._nombre} | {self._temperatura.value} | "
                f"{self._tamaño.value} | ${self._precio:,.0f}")

@dataclass
class BebidaCaliente(Bebida):

    def preparar(self) -> str:
        return f"Calentando {self._nombre} tamaño {self._tamaño.value}..."


@dataclass
class BebidaFria(Bebida):

    def preparar(self) -> str:
        return f"Enfriando {self._nombre} tamaño {self._tamaño.value}..."
    