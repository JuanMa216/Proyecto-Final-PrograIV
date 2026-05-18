from patterns.decorator.bebida_base import Bebida


class DecoradorBebida(Bebida):

    def __init__(self, bebida):
        self.bebida = bebida