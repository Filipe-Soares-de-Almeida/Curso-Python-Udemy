# Exercicio com funções

# Crie uma função que multiplica todos os argumentos não nomeados recebidos
# Retorne o total para uma variável e mostre o valor da variável

def multiplica(*args):
  total = 1
  for n in args:
    total *= n

  return total

multiplicacao = multiplica(1, 4, 6, 43, 2, 6)
print(multiplicacao)


# Crie uma função que fala se um numero é par ou ímpar
# Retorne se o numero é par ou ímpar
def par_impar(numero):
  return 'Par' if numero % 2 == 0 else 'Ímpar'

print(par_impar(4))