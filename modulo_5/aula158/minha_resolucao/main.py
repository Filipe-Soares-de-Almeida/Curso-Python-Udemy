from banco import Banco
from cliente import Cliente
from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

pedro = Cliente('Pedro', 20)
pedro.conta = ContaCorrente(1234, 5)

joao = Cliente('João', 23)
joao.conta = ContaPoupanca(1234, 2)

maria = Cliente('Maria', 25)
maria.conta = ContaCorrente(1111, 15)

banco_do_brasil = Banco('Banco do Brasil')
banco_do_brasil.adicionar_agencias([1, 2, 3, 4])
banco_do_brasil.adicionar_contas([1234, 2222, 4356])
banco_do_brasil.adicionar_clientes([pedro, joao, maria])


santander = Banco('Santander')
santander.adicionar_agencias([5, 7, 8, 9, 10])
santander.adicionar_contas([1234, 2222, 4356])
santander.adicionar_clientes([pedro, joao, maria])

sicoob = Banco('Sicoob')
sicoob.adicionar_agencias([11, 12, 13, 14, 15])
sicoob.adicionar_contas([1234, 2222, 1111])
sicoob.adicionar_clientes([joao, maria])

def tentar_sacar(banco: Banco, cliente: Cliente, valor: int | float):
  try:
    banco.sacar(cliente, valor)
  except ValueError as error:
    print(error)

def tentar_depositar(banco: Banco, cliente: Cliente, valor: int | float):
  try:
    banco.depositar(cliente, valor)
  except ValueError as error:
    print(error)

def tentar_verificar_extrato(banco: Banco, cliente: Cliente):
  try:
    banco.verificar_extrato(cliente)
  except ValueError as error:
    print(error)

def realizar_operacoes(bancos: list[Banco], cliente_valor: list[tuple[Cliente, int | float]]):
  for banco in bancos:
    for cliente, valor in cliente_valor:
      tentar_depositar(banco, cliente, valor)
      tentar_sacar(banco, cliente, valor)
      tentar_verificar_extrato(banco, cliente)
      print('-' * 50)


realizar_operacoes(
  [banco_do_brasil, santander, sicoob],
  [(joao, 1000), (maria, 5000), (pedro, 200)]
)
