""" Calculadora com while """
while True:
  num1 = input("Digite o primeiro numero: ")
  num2 = input("Digite o segundo numero: ")
  operador = input("Digite o operador (+, -, *, /): ")
  
  num_valido = None;
  try:
    num1 = float(num1)
    num2 = float(num2)
    num_valido = True;
  except:
    num_valido = False;
    
  if not num_valido:
    print("Um ou ambos os numeros não são validos!")
    continue;
    
  resultado = None;
  if operador in ['+', '-', '*', '/']:
    if operador == '/':
      resultado = num1 / num2
    elif operador == '*':
      resultado = num1 * num2
    elif operador == '-':
      resultado = num1 - num2
    elif operador == '+':
      resultado = num1 + num2
  else:
    print('Isso nao e uma operacao valida!'); 
    continue;
    
  print(f'O resultado foi {resultado}')
  
  if input("Quer fazer outro calculo? (s/n): ").lower() == 'n':   
    break
    
print('Fim do programa')