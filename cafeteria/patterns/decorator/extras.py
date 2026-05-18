from patterns.decorator.decorator_base import DecoradorBebida
from patterns.decorator.bebida_base import Bebida


class Latte(Bebida):

    def costo(self):
        return 5000


class ExtraEspresso(DecoradorBebida):

    def costo(self):
        return self.bebida.costo() + 2000


class Caramelo(DecoradorBebida):

    def costo(self):
        return self.bebida.costo() + 1500