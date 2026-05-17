# models/persona.py
# Patron: N/A (clase base de datos)
#
# TODO: Clase Persona
#   - TODO: Atributos: id, nombre, email, telefono
#   - TODO: Metodo __str__() que devuelva representacion en cadena
from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Persona(ABC):
    _nombre: str
    _apellido: str
    _email: str
    _password: str

    @property
    def nombre(self):
        return self._nombre

    @property 
    def apellido(self):
        return self._apellido

    @property
    def email(self):
        return self._email

    @property
    def password(self):
        return self._password

    @password.setter 
    def password(self, nueva):
        if len(nueva) < 6:
            raise ValueError("La contraseña debe tener al menos 6 caracteres")
        self._password = nueva

    @abstractmethod
    def get_rol(self) -> str:
        pass

    def __str__(self):
        return f"{self._nombre} {self._apellido} ({self.get_rol()})"