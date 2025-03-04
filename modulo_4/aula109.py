"""
Combinations, Permutations e Product - Itertools
Combinação - Ordem não importa - iteravel + tamanho do grupo
Permutação - Ordem importa
Produto - Ordem importa e repete valores unicos
"""
from itertools import combinations, permutations, product

def pretty_print(iterable):
  print(*list(iterable), sep='\n')
  print()

pessoas = [
  'João', 'Joana', 'Luiz', 'Leticia'
]

camisetas = [
  ['preta', 'branca'],
  ['P', 'M', 'G'],
  ['masculino', 'feminino', 'unisex'],
  ['algodão', 'poliester'],
]

# pretty_print(combinations(pessoas, 2))
# pretty_print(permutations(pessoas, 2))

pretty_print(product(*camisetas))
