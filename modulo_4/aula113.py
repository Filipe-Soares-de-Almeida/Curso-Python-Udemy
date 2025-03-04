# reduce - reduzindo um iterável a um valor unico
from functools import reduce

def pretty_print(iterator):
  print(*list(iterator), sep='\n')
  print()

produtos = [
  {'nome': 'Produto 5', 'preco': 10},
  {'nome': 'Produto 1', 'preco': 22.32},
  {'nome': 'Produto 3', 'preco': 10.11},
  {'nome': 'Produto 2', 'preco': 105.87},
  {'nome': 'Produto 4', 'preco': 69.90}
]

def funcao_do_reduce(acumulador, produto):
  return acumulador + produto['preco']

soma_produtos = reduce(
  funcao_do_reduce,
  produtos,
  0
)

print(soma_produtos)