# Problema dos parametros mutaveis em funções Python

def adiciona_clientes(nome, lista=None):
  if lista is None:
    lista = []

  lista.append(nome)
  return lista

clientes1 = adiciona_clientes('Joao')
adiciona_clientes('Maria', clientes1)

clientes2 = adiciona_clientes('Pedro')
adiciona_clientes('Ana', clientes2)


print(clientes1)
print(clientes2)