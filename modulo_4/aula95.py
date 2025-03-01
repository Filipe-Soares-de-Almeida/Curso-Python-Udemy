# raises - lançando exceções (erros)

def valida_zero_division(x):
  if x == 0:
    raise ZeroDivisionError("Divisão por zero")
  
  return True

def valida_tipo(number):
  if not isinstance(number, (int, float)): 
    raise TypeError(
      f'{number} deve ser do tipo int ou float '
      f'({type(number).__name__} informado)'
    )
  
  return True


def divide(x, y):
  valida_tipo(x)
  valida_tipo(y)
  
  valida_zero_division(y)

  return x / y


print(divide('1', 0))