from conta import Conta

class ContaPoupanca(Conta):
  def __init__(self, numero: int, agencia: int):
    super().__init__(numero, agencia)

  def sacar(self, valor: int | float):
    if self._saldo >= valor:
      self._saldo -= valor
      print(f"Saque de {valor} efetuado com sucesso!\n")
    else:
      print(f"Saldo insuficiente para saque de {valor}!\n")
