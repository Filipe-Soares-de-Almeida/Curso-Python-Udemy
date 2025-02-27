"""
Lambda Functions

Lambda functions são funções anônimas que podem ser usadas como argumentos em outras funções, 
ou podem ser retornadas por outras funções. 
Isso permite criar funções mais dinamicas e flexiveis, 
pois podem ser usadas em diferentes contextos.

A sintaxe de uma função lambda é a seguinte:
lambda arguments: expression

Exemplo:
soma = lambda x, y: x + y
print(soma(1, 2)) # 3

lista = [
 {'nome': 'João', 'idade': 25},
 {'nome': 'Maria', 'idade': 30},
 {'nome': 'Pedro', 'idade': 20}
 {'nome': 'Ana', 'idade': 35}
]
"""


lista = [
 {'nome': 'João', 'idade': 25},
 {'nome': 'Maria', 'idade': 30},
 {'nome': 'Pedro', 'idade': 20},
 {'nome': 'Ana', 'idade': 35}
]

lista.sort(key=lambda x: x['idade'])
print(lista)