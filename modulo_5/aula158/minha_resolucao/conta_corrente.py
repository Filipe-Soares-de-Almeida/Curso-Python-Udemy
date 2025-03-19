from conta import Conta

class ContaCorrente(Conta):
  def __init__(self, numero, agencia):
    super().__init__(numero, agencia)
    self._limite = 500

  def sacar(self, valor):
    if self._saldo >= valor:
      self._saldo -= valor
      print(f"Saque de {valor} efetuado com sucesso!\n")
    elif self._saldo + self._limite >= valor:
      self._limite -= (valor - self._saldo)
      self._saldo = 0
      print(f"Saque de {valor} efetuado com sucesso!\n")
    else:
      print(f"Saldo insuficiente para saque de {valor}!\n")
