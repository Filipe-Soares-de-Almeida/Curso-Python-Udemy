# dir, hasattr e getattr em Python

"""
dir - mostra todos os atributos e métodos de um objeto
hasattr - verifica se um objeto possui um atributo ou método
getattr - retorna o valor de um atributo de um objeto
"""

texto = 'texto simples'

if hasattr(texto, 'upper'):
  print(getattr(texto, 'upper')())  
  