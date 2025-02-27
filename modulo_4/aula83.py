"""
Desempacotamento e empacotamento de dicionarios
"""

#Desempacotamento de dicionarios
pessoa = {'nome': 'Joao', 'idade': 25}
nome, idade = pessoa.values()
print(nome, idade)

#Empacotamento de dicionarios
pessoa = {'nome': 'Joao', 'idade': 25}
nome, idade = pessoa.keys()
print(nome, idade)

# Exemplo de desempacotamento de dois dicionários em um terceiro usando kwargs

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

# Unpack the dictionaries into a new one
merged_dict = {**dict1, **dict2}

print(merged_dict)


#Kwargs
def soma(**kwargs):
  """
  Soma todos os valores presentes no dicionario recebido como parametro
  
  Args:
    **kwargs: dicionario com os valores a serem somados
  
  Returns:
    int: soma de todos os valores
  """
  total = 0
  for chave, valor in kwargs.items():
    total += valor
  return total

print(soma(a=1, b=2, c=3)) #6