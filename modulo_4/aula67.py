"""
Valores padrão para parâmetros
ao definir uma função, os parametros podem ter valores padrao
Caso o valor não seja enviado para o parametro, o valor padrao será usado
"""


def soma(x, y):
  print(x + y)
  
  
def soma_vlr_padrao(x, y=2):
  print(x + y)
  

def soma_vlr_padrao_none(x, y, z=None):
  if z is None: 
    print(x + y)
  else:
    print(x + y + z)
    
  
  
  
soma(10, 20)
soma_vlr_padrao(10)
soma_vlr_padrao(10, 20)


soma_vlr_padrao_none(10, 20)
soma_vlr_padrao_none(10, 20, 30)