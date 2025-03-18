"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra.

Conta (ABC)
    ContaCorrente
    ContaPoupanca

Pessoa (ABC)
    Cliente
        Cliente -> Conta

Banco
    Banco -> Cliente
    Banco -> Conta

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)

Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)

Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
Banco autentica por um método.
"""
from abc import ABC, abstractmethod

class Conta(ABC):
  def __init__(self, numero, agencia, cliente):
    self._numero = numero
    self._agencia = agencia
    self._cliente = cliente
    self._saldo = 0

  @abstractmethod
  def sacar(self, valor):
    ...

  def depositar(self, valor):
    self.saldo += valor
    print(f'Deposito de {valor} efetuado com sucesso!')

  def extrato(self):
    print(
      '*' * 10 + f'Extrato de {self._cliente.nome}' + '*' * 10 + '\n'
      f'Agência: {self._agencia}\n'
      f'Conta: {self._numero}\n'
      f'Saldo: {self._saldo}'
    )

class ContaCorrente(Conta):
  def __init__(self, numero, agencia, cliente):
    super().__init__(numero, agencia, cliente)
    self._limite = 500

  def sacar(self, valor):
    if self._saldo >= valor:
      self._saldo -= valor
      print(f'Saque de {valor} efetuado com sucesso!')
    elif self._saldo + self._limite >= valor:
      self._saldo = 0
      self._limite -= (valor - self._saldo)
      print(f'Saque de {valor} efetuado com sucesso!')
    else:
      print(f'Saldo insuficiente para saque de {valor}!')

class ContaPoupanca(Conta):
  def __init__(self, numero, agencia, cliente):
    super().__init__(numero, agencia, cliente)

  def sacar(self, valor):
    if self._saldo >= valor:
      self._saldo -= valor
      print(f'Saque de {valor} efetuado com sucesso!')
    else:
      print(f'Saldo insuficiente para saque de {valor}!')

class Pessoa(ABC):
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  @property
  def nome(self):
    return self._nome

  @nome.setter
  def nome(self, nome):
    self._nome = nome

  @property
  def idade(self):
    return self._idade

  @idade.setter
  def idade(self, idade):
    self._idade = idade

class Cliente(Pessoa):
  def __init__(self, nome, idade):
    super().__init__(nome, idade)
    self.conta = None

  @property
  def conta(self):
    return self._conta

  @property
  def conta(self, conta):
    self._conta = conta

class Banco:
  def __init__(self, nome):
    self._nome = nome
    self._clientes = []
    self._contas = []
    self._agencias = []

  def adicionar_clientes(self, clientes):
    self._clientes.extend(clientes)

  def adicionar_contas(self, contas):
    self._contas.extend(contas)

  def adicionar_agencias(self, agencias):
    self._agencias.extend(agencias)

  def autenticar(self, cliente: Cliente):
    if not cliente in self._clientes:
      raise ValueError(
        f'Cliente {cliente} não cadastrado no banco: {self._nome}'
      )

    if not cliente.conta in self._contas:
      raise ValueError(
        f'Conta {cliente.conta} não encontrada no banco: {self._nome}'
      )

    if not cliente.conta._agencia in self._agencias:
      raise ValueError(
        f'Agência {cliente.conta._agencia} não encontrada no banco: {self._nome}'
      )

pedro = Cliente('Pedro', 20)
pedro.conta = ContaCorrente(1234, 5, pedro)

joao = Cliente('João', 23)
joao.conta = ContaPoupanca(1234, 2, joao)

maria = Cliente('Maria', 25)
maria.conta = ContaCorrente(1111, 2, maria)


banco_do_brasil = Banco('Banco do Brasil')
banco_do_brasil.adicionar_agencias([1, 2, 3, 4, 5])

santander = Banco('Santander')
sicoob = Banco('Sicoob')
