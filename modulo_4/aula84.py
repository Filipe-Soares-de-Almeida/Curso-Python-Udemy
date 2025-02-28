# List Comprehension em Python

# List comprehension é uma maneira concisa de criar listas. 
# Ela permite criar listas a partir de iteráveis de forma clara e concisa. 
# A sintaxe básica de uma list comprehension é:

# [expressão for item in iterável if condição]

# Onde "expressão" é o valor que será adicionado à lista, 
# "item" é uma variável que representa cada elemento do iterável, 
# e "condição" é opcional, que filtra os elementos do iterável.

# Exemplo 1: Criar uma lista de quadrados de números de 0 a 9
quadrados = [x**2 for x in range(10)]
print(quadrados)  # Saída: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Exemplo 2: Criar uma lista com números pares de 0 a 9
pares = [x for x in range(10) if x % 2 == 0]
print(pares)  # Saída: [0, 2, 4, 6, 8]



# Exemplo 3: Mapear uma lista de nomes para uma lista de inicial (primeira letra)
nomes = ['Joao', 'Maria', 'Pedro', 'Ana']
iniciais = [nome[0] for nome in nomes]
print(iniciais)  # Saída: ['J', 'M', 'P', 'A']

# O que está acontecendo?
# A list comprehension está mapeando cada elemento da lista nomes para o primeiro caractere do elemento.
# Em outras palavras, a list comprehension está criando uma lista de inicial (primeira letra) para cada nome da lista nomes


produtos = [
  {'nome': 'Produto 1', 'preco': 10},
  {'nome': 'Produto 2', 'preco': 20},
  {'nome': 'Produto 3', 'preco': 30},	           
]

novos_produtos = [
  {**produto, 'preco': produto['preco'] * 1.1}
  if produto['preco'] > 20 else {**produto}
  for produto in produtos
]

print(*novos_produtos, sep='\n')