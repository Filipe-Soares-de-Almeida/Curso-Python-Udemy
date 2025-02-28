# isinstance - Verifica se um objeto pertence é um determinado tipo

lista = ['a', 1, 1.1, True, [0,1,2], (1,2), {0, 1}, {'nome': 'João'}]

def RetornaTipo(item):
   if isinstance(item, str):
      return 'uma String'
   elif isinstance(item, int):
      return 'um Inteiro'
   elif isinstance(item, float):
      return 'um Float'
   elif isinstance(item, bool):
      return 'um Booleano'
   elif isinstance(item, list):
      return 'uma Lista'
   elif isinstance(item, tuple):
      return 'uma Tupla'
   elif isinstance(item, set):
      return 'um Set'
   elif isinstance(item, dict):
      return 'um Dicionário'
   else:
      return 'Tipo desconhecido'


for item in lista:
  print(f'O item {item} é {RetornaTipo(item)}')

  