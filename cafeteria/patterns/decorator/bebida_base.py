from abc import ABC, abstractmethod


class Bebida(ABC):

    @abstractmethod
    def descripcion(self):
        pass

    @abstractmethod
    def costo(self):
        pass