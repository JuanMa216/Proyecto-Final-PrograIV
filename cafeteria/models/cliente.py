# models/cliente.py
# Patron: N/A (modelo de dominio)
#
# TODO: Clase Cliente
#   - TODO: Atributos: id, nombre, puntos_fidelidad, es_frecuente
#   - TODO: Metodo acumular_puntos(monto) que sume puntos segun el monto
#   - TODO: Metodo canjear_puntos(puntos) que reste puntos disponibles
from dataclasses import dataclass, field
from models.persona import Persona

@dataclass 
class Cliente(Persona):
    _id_cliente: int
    _puntos_fidelidad: int = 0

    @property
    def id_cliente(self):
        return self._id_cliente

    def puntos_fidelidad(self):
        return self._puntos_fidelidad
    
    def get_rol(self) -> str:
        return "Cliente"

    def agregar_puntos(self, puntos: int):
        if puntos < 0:
            raise ValueError("Los puntos no pueden ser negativos")
        self._puntos_fidelidad += puntos

    def canjear_puntos(self, puntos: int):
        if puntos > self._puntos_fidelidad:
            raise ValueError("Puntos insuficientes") 
        self._puntos_fidelidad -= puntos

    def __str__(self):
        return f"{self._nombre} {self._apellido} | Puntos: {self._puntos_fidelidad}"
