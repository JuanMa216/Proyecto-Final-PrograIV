from abc import ABC, abstractmethod


class Bebida(ABC):

    @abstractmethod
    def costo(self):
        pass