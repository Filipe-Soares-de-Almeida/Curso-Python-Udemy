# Exercicios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (copia profunda)
from copy import deepcopy


produtos = [
  {'nome': 'Produto 5', 'preco': 10},
  {'nome': 'Produto 1', 'preco': 22.32},
  {'nome': 'Produto 3', 'preco': 10.11},
  {'nome': 'Produto 2', 'preco': 105.87},
  {'nome': 'Produto 4', 'preco': 69.90}
]

novos_produtos = [{**produto, 'preco': round(produto['preco'] * 1.1, 2)} for produto in deepcopy(produtos)]

print('Produtos:')
print(*produtos, sep='\n')

print()

print('Novos produtos:')
print(*novos_produtos, sep='\n')

print()
# Ordene os produtos por nome decrescente (do maior para o menor)
# gere produtos_ordenados_por_nome por deep copy (copia profunda)
produtos_ordenados_por_nome = sorted(deepcopy(produtos), key=lambda produto: produto['nome'], reverse=True)

print('Produtos ordenados por nome:')
print(*produtos_ordenados_por_nome, sep='\n')

print()
# Ordene os produtos por preco crescente (do menor para o maior)
# gere produtos_ordenados_por_preco por deep copy (copia profunda)
produtos_ordernados_por_preco = sorted(deepcopy(produtos), key=lambda produto: produto['preco'])

print('Produtos ordenados por preco:')  
print(*produtos_ordernados_por_preco, sep='\n')