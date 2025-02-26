# Exemplo de uso do sets

letras = set()

while True:
  letra = input('Digite: ')
  letras.add(letra)

  print(letras)

  if 'l' in letras:
    print('P')
    break

  print(letras)