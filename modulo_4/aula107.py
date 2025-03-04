"""
Exercicios - Unir listas
Crie uma função zipper (como o zipper de roupas)
O trabalho dessa função será unir duas listas na ordem
Use todos os valores da menor lista.

Exemplo:

['Salvador', 'Ubatuba', 'Belo Horizonte']
['BA', 'SP', 'MG', 'RJ']

Resultado: [('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]

""" 
lista_cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
lista_estados = ['BA', 'SP', 'MG', 'RJ']


def zipper_factory():
  def zipper_decorator(func):
    def inner(lista_1, lista_2):
      len1 = len(lista_1)
      len2 = len(lista_2)
      lista_len = len1 if len1 < len2 else len2

      result = [func(lista_1[i], lista_2[i]) for i in range(0, lista_len)]
      return result
   
    return inner
  return zipper_decorator

@zipper_factory()
def zipper(v1, v2):
  return v1, v2


lista_final = zipper(lista_cidades, lista_estados)

print(lista_final)




"""
Considerando duas listas de inteiros ou floats (lista A e lista B)
some os valores nas listas retornando uma nova lista com os valores somados?

se uma lista for maior que a outra a soma só vai considerar o tamanho da menor

exemplo:
lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]

resultado = [2, 4, 6, 8]

"""

lista_a = [1, 2, 3, 4, 5, 6, 7]
lista_b = [1, 2, 3, 4]


def soma_listas(lista_a, lista_b):
  intervalo = min(len(lista_a), len(lista_b))
  return [lista_a[i] + lista_b[i] for i in range(intervalo)]


lista_soma = soma_listas(lista_a, lista_b)
print(lista_soma)