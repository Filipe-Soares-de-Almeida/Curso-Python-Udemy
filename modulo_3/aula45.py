"""
Iteravel -> Str, range, etc
Iterador -> quem sabe entregar um valor por vez
next -> proximo valor
iter -> iterador
"""

texto = 'catapimbas' # iteravel
texto_iterador = iter(texto) # iterador

while True:
  try:
    letra = next(texto_iterador)
    print(letra)
  except StopIteration:
    break