
from cliente import Cliente


class Banco:
  def __init__(self, nome):
    self._nome: str = nome
    self._clientes: list = []
    self._contas: list = []
    self._agencias: list = []

  def adicionar_clientes(self, clientes: list):
    self._clientes.extend(clientes)

  def adicionar_contas(self, contas: list):
    self._contas.extend(contas)

  def adicionar_agencias(self, agencias: list):
    self._agencias.extend(agencias)

  def autenticar(self, cliente: Cliente):
    if cliente not in self._clientes:
      raise ValueError(
          f"Cliente {cliente.nome} não cadastrado no banco: {self._nome}\n")

    if cliente.conta._numero not in self._contas:
      raise ValueError(
          f"Conta {cliente.conta._numero} para o cliente {cliente.nome} não encontrada no banco: {self._nome}\n")

    if cliente.conta._agencia not in self._agencias:
      raise ValueError(
          f"Agência {cliente.conta._agencia} da conta {cliente.conta._numero} para o cliente {cliente.nome} não encontrada no banco: {self._nome}\n")

    self.autenticado = True

    print(
      f"Cliente {cliente.nome} autenticado com sucesso! "
      f"(Banco: {self._nome})"
    )

  def sacar(self, cliente: Cliente, valor: int | float):
    self.autenticar(cliente)
    cliente.conta.sacar(valor)

  def depositar(self, cliente: Cliente, valor: int | float):
    self.autenticar(cliente)
    cliente.conta.depositar(valor)

  def verificar_extrato(self, cliente: Cliente):
    self.autenticar(cliente)
    cliente.conta.extrato()
