import pprint

def log(printable):
  pprint.pprint(printable, width=50, compact=False, sort_dicts=False)

# Dictionary Comprehension e Set Comprehension

produto = {
  'nome': 'Caneta Azul',
  'preco': 2.5,
  'categoria': 'Escritório' 
}

dc = {
  chave: valor.upper()
  if isinstance(valor, (str)) else valor
  for chave, valor in produto.items()
}

log(dc)

s1 = {i for i in range(10)}

