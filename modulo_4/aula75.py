# Exercicios
# Crie funções que duplicam, triplicam e quadriplicam o numero recebido como parametro


def criar_multiplicador(multiplicador):
  def multiplica(numero):
    return numero * multiplicador
  return multiplica

duplica = criar_multiplicador(2)
triplica = criar_multiplicador(3)
quadriplica = criar_multiplicador(4)

print(duplica(2))
print(triplica(2))
print(quadriplica(2))