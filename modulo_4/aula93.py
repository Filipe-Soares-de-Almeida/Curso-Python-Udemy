# try, except, else e finally



try:
  ...
except:
  ...

try:
  ...
finally:
  ...


try:
  print(1)
except:
  print(2)
else:
  print(3)
finally:
  print(4)



try:
  a = 18
  b = 0
  # print(b[0])
  print('Linha 1')
  # c = a / b
  print('Linha 2')

  string = 'batata'
  string[2300]
except ZeroDivisionError:
  print('Dividiu por zero')
except NameError:
  print( 'Nome b não está definido')
except TypeError:
  print( 'TypeError')
except Exception as erro:
  print('ERRO DESCONHECIDO: ' + erro.__class__.__name__)

print('CONTINUAR ')  


