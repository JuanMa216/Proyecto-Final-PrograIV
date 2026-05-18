from patterns.decorator.decorator_base import DecoradorBebida
from patterns.decorator.bebida_base import Bebida


class ProductoBase(Bebida):

    def __init__(self, producto):
        self.producto = producto

    def descripcion(self):
        return self.producto.nombre

    def costo(self):
        return self.producto.precio


class ExtraDecorator(DecoradorBebida):

    def __init__(self, bebida, nombre_extra, precio_extra):
        super().__init__(bebida)
        self.nombre_extra = nombre_extra
        self.precio_extra = precio_extra

    def descripcion(self):
        return f"{self.bebida.descripcion()} +{self.nombre_extra}"

    def costo(self):
        return self.bebida.costo() + self.precio_extra