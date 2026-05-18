from patterns.decorator.bebida_base import Bebida


class DecoradorBebida(Bebida):

    def __init__(self, bebida):
        self.bebida = bebida

    def descripcion(self):
        return self.bebida.descripcion()

    def costo(self):
        return self.bebida.costo()