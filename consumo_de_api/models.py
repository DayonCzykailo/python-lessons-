from abc import ABC, abstractmethod


class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    @abstractmethod
    def metodo_abstrato(self):
        pass

    @property
    def showNome(self) -> str :
        return self._nome.title()

class Prato(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def metodo_abstrato(self):
        pass

class Bebida(ItemCardapio):
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self._descricao = descricao

    def metodo_abstrato(self):
        pass