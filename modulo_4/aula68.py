"""
Escopo de funções em Python

Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e o local.
O escopo global é o escopo onde todo o codigo é alcançável.
O escopo local é o escopo onde o codigo so pode ser atingido quando estiver dentro do bloco que o contem.
"""

x = 1

def meu_escopo_local():
  x = 10 # escopo local
  print("Escopo local: ", x)

meu_escopo_local()
print("Escopo global: ", x) # vai dar erro pois x nao esta disponivel no escopo global



x = 100 # escopo global

def meu_escopo_local():
  global x # agora x é global
  x += 1 # incrementa o valor de x
  print("Escopo local: ", x)

meu_escopo_local()
print("Escopo global: ", x) # vai printar 101
