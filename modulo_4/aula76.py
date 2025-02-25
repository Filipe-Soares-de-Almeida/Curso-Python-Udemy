"""
Dicionarios em Python (tipo dict)

Dicionarios sao estruturas de dados compostas por chave e valor.
A chave serve como identificador para o valor.
A chave pode pode ser composta dos tipos imutaveis (int, float, bool, str, tuple)
O valor pode ser de qualquer tipo (inclusive outro dicionario).
Dicionarios sao mutaveis, ou seja, podem ser alterados.
Dicionarios sao iteraveis, ou seja, podem ser percorridos.
Dicionarios sao objetos, ou seja, podem ser passados como argumentos para funcoes.
Dicionarios sao representados por colchetes {}.

Exemplo:
pessoa = {
    'nome': 'Joao',
    'idade': 30,
    'endereco': {
        'rua': 'Rua do Joao',
        'bairro': 'Bairro do Joao'
    }
}

print(pessoa['nome']) # imprime Joao
print(pessoa['idade']) # imprime 30
print(pessoa['endereco']['rua']) # imprime Rua do Joao
print(pessoa['endereco']['bairro']) # imprime Bairro do Joao

funções uteis do dicionario:

keys() - retorna as chaves do dicionario
values() - retorna os valores do dicionario
items() - retorna uma lista de tuplas com chaves e valores
get() - retorna o valor da chave passada, se nao encontrar retorna None ou o valor padrao
pop() - retorna e remove o valor da chave passada
popitem() - retorna e remove a ultima chave e valor do dicionario
clear() - limpa o dicionario
update() - atualiza o dicionario com os valores do outro dicionario

"""

pessoa = {
  'nome': 'Joao',
  'idade': 30,
  'endereco': {
    'rua': 'Rua do Joao',
    'bairro': 'Bairro do Joao'
  }
}
print(pessoa['nome']) # imprime Joao
print(pessoa['idade']) # imprime 30
print(pessoa['endereco']['rua']) # imprime Rua do Joao

pessoa2 = {}
pessoa2['nome'] = 'Maria'
pessoa2['idade'] = 25
pessoa2['endereco'] = {
  'rua': 'Rua da Maria',
  'bairro': 'Bairro da Maria'
}
print(pessoa2['nome']) # imprime Maria
print(pessoa2['idade']) # imprime 25
print(pessoa2['endereco']['rua']) # imprime Rua da Maria

del pessoa2['endereco']
print(pessoa2)


# shallow copy
import copy

d1 = {
  'a': 1, 
  'b': 2,
  'c': {
    'd': 3
  }
}

d2 = copy.copy(d1)

d1['c']['d'] = 4

print(d1) # {'a': 1, 'b': 2, 'c': {'d': 4}}
print(d2) # {'a': 1, 'b': 2, 'c': {'d': 4}}

# deep copy
d3 = copy.deepcopy(d1)

d1['c']['d'] = 5

print(d1) # {'a': 1, 'b': 2, 'c': {'d': 5}}
print(d3) # {'a': 1, 'b': 2, 'c': {'d': 4}}

