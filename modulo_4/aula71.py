"""
args - argumentos nao nomeados
* - *args (empacotamento e desempacotamento)
"""

#lembrete de desempacotamento
x, y, *resto = 1, 2, 3, 4, 5

print(x, y, *resto)

def soma(x, y):
  return x + y


def soma_com_args(*args):
  
  result = 0
  
  for i in args:
    result += i
    
  return result

print(soma_com_args(1, 2, 3, 4, 5))
