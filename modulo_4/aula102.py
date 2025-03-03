# Variaveis livres + nonlocal

# def fora():
#   a = 1
#   def dentro():
#     return a
  
#   return dentro()

# dentro = fora()


def concatenar(str_inicial):
  str_concatenada = str_inicial

  def interna(str_adicionar):
    nonlocal str_concatenada
    str_concatenada += str_adicionar

    return str_concatenada
  
  return interna

c = concatenar('a')

print(c('b'))