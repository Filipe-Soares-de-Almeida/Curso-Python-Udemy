"""
Introdução ao try/except

try -> tentar executar o codigo
except -> ocorreu algum erro na execução
"""

try:
  numero_str = input('Vou dobrar o número que você digitar: ')
  print(f'{numero_str=}')
  
  numero_float = float(numero_str)
  print(f'{numero_float=}')
  
  print(f'O numero {numero_str} dobrado é {numero_float * 2}!')

except:
  print('Isso não é um número!')