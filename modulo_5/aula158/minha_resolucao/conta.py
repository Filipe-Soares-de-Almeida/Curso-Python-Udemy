from abc import ABC, abstractmethod

class Conta(ABC):
  def __init__(self, numero, agencia):
    self._numero: int = numero
    self._agencia: int = agencia
    self._saldo: int | float = 0

  @abstractmethod
  def sacar(self, valor: int | float):
    ...

  def depositar(self, valor: int | float):
    self._saldo += valor
    print(f"Depósito de {valor} efetuado com sucesso!\n")

  def extrato(self):
    print(
      f"Agência: {self._agencia}\nConta: {self._numero}\nSaldo: {self._saldo:.2f}")
