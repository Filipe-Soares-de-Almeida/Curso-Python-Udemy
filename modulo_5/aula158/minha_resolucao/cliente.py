from pessoa import Pessoa
from conta import Conta

class Cliente(Pessoa):
  def __init__(self, nome: str, idade: int):
    super().__init__(nome, idade)
    self.conta: Conta = None
