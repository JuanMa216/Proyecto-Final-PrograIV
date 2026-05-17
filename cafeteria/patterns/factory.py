# patterns/factory.py
# Patron: Factory Method
#
# TODO: Clase ProductoFactory
#   - TODO: Metodo estatico crear_producto(tipo, **kwargs) que instancie:
#     - TODO: "BebidaCaliente" -> BebidaCaliente
#     - TODO: "BebidaFria" -> BebidaFria
#     - TODO: "Pasteleria" -> Pasteleria
#     - TODO: "Snack" -> Snack
# patterns/factory.py
# Patrón: Factory Method

from models.bebida import BebidaCaliente, BebidaFria, Temperatura, Tamaño
from models.comida import Pasteleria, Snack


class ProductoFactory:

    #Registro de tipos disponibles
    _tipos = {
        "bebida_caliente": BebidaCaliente,
        "bebida_fria": BebidaFria,
        "pasteleria": Pasteleria,
        "snack": Snack,
    }

    @classmethod
    def crear(cls, tipo: str, **kwargs):
        """
        Crea y retorna un producto según el tipo indicado.
        
        Uso:
            ProductoFactory.crear("bebida_caliente",
                _nombre="Latte",
                _precio=5000,
                _categoria="Bebidas calientes",
                _descripcion="Café con leche",
                _temperatura=Temperatura.CALIENTE,
                _tamaño=Tamaño.MEDIANO
            )
        """
        tipo = tipo.lower().strip()

        if tipo not in cls._tipos:
            tipos_validos = ", ".join(cls._tipos.keys())
            raise ValueError(
                f"Tipo '{tipo}' no válido. Tipos disponibles: {tipos_validos}"
            )

        clase = cls._tipos[tipo]
        return clase(**kwargs)

    @classmethod
    def tipos_disponibles(cls) -> list:
        return list(cls._tipos.keys())