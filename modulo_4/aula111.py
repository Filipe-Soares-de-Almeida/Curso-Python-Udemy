from functools import partial


def pretty_print(iterator):
  print(*list(iterator), sep='\n')
  print()

def aumenta_porcentagem(valor, porcentagem):
  return round(valor * porcentagem, 2)

aumenta_dez_porcento = partial(
  aumenta_porcentagem,
  porcentagem=1.1
)

def muda_preco_produto(produto):
  return {
    **produto,
    'preco': aumenta_dez_porcento(produto['preco'])
  }


produtos = [
  {'nome': 'Produto 5', 'preco': 10},
  {'nome': 'Produto 1', 'preco': 22.32},
  {'nome': 'Produto 3', 'preco': 10.11},
  {'nome': 'Produto 2', 'preco': 105.87},
  {'nome': 'Produto 4', 'preco': 69.90}
]

novos_produtos = map(muda_preco_produto, produtos)

pretty_print(novos_produtos)