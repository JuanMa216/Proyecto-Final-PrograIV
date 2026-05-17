# models/empleado.py
# Patron: N/A (modelo de dominio)
#
# TODO: Clase Empleado (hereda de Persona)
#   - TODO: Atributos: username, password, puesto, salario, fecha_contratacion
#   - TODO: Propiedades con getters y setters para puesto, salario
#   - TODO: Metodo validar_credenciales(username, password)
#
# TODO: Clase Administrador (hereda de Empleado)
#   - TODO: Constructor que fije puesto como "Administrador"
#
# TODO: Clase Cajero (hereda de Empleado)
#   - TODO: Constructor que fije puesto como "Cajero"
#
# TODO: Clase Barista (hereda de Empleado)
#   - TODO: Constructor que fije puesto como "Barista"
from dataclasses import dataclass
from models.persona import Persona

@dataclass
class Empleado(Persona):
    _id_empleado: int 
    _cargo: str
    _salario: float
    _activo: bool = True

    @property
    def id_empleado(self):
        return self._id_empleado

    @property
    def cargo(self):
        return self._cargo

    @property
    def salario(self):
        return self._salario

    @property
    def activo(self):
        return self._activo

    @salario.setter
    def salario(self, nuevo): 
        if nuevo < 0:
            raise ValueError("El salario no puede ser negativo")
        self._salario = nuevo

    @activo.setter
    def activo(self, valor: bool):
        self._activo = valor

    def get_rol(self) -> str:
        return self._cargo

    def __str__(self):
        estado = "Activo" if self._activo else "Inactivo"
        return f"{self._nombre} {self._apellido} | {self._cargo} | {estado}"

@dataclass
class Barista(Empleado):

    def get_rol(self) -> str:
        return "Barista"

    def preparar_pedido(self, pedido_id: int) -> str:
        return f"Pedido #{pedido_id} en preparacion por {self._nombre}" 

@dataclass 
class Cajero(Empleado):

    def get_rol(self) -> str:
        return "Cajero"

    def procesar_pago(self, total: float) -> str:
        return f"Pago de ${total:,.0f} procesado por {self._nombre}"

@dataclass
class Administrador(Empleado):

    def get_rol(self) -> str:
        return "Administrador"

    def generar_reporte(self) -> str:
        return f"Reporte generado por {self._nombre}"