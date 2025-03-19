from abc import ABC

class Pessoa(ABC):
  def __init__(self, nome: str, idade: int):
    self._nome: str = nome
    self._idade: int = idade

  @property
  def nome(self):
    return self._nome

  @property
  def idade(self):
    return self._idade
