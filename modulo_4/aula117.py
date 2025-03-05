"""
JSON em Python

JSON - JavaScript Object Notation -  uma linguagem de marcação de dados human-readable,
usada para armazenar e transmitir dados entre sistemas.

A linguagem JSON é uma forma de representar dados em um formato de texto, 
que é fãcil de ler e escrever, e é mais leve que linguagens como XML.

Um arquivo JSON é composto por chaves e valores, onde cada chave é uma string,
e cada valor pode ser um numero, string, booleano, array, objeto ou nulo.

Em Python, o modulo `json` é usado p/ trabalhar com arquivos JSON.

O modulo `json` é usado p/ converter um dicionário python em um arquivo JSON,
e vice-versa. Além disso, o modulo `json` é usado p/ carregar e salvar arquivos JSON.

"""
import json


# pessoa = {
#   'nome': 'Tatupeba',
#   'idade': 18,
#   'enderecos': [
#     {'rua': 'Rua do Tatupeba', 'bairro': 'Bairro do Tatupeba'},
#     {'rua': 'Rua do Tatupeba 2', 'bairro': 'Bairro do Tatupeba'}
#   ],
#   'altura': 0.95,
#   'dev': True,
#   'nada': None,
# }

with open('aula117.json', 'r', encoding='utf-8') as arquivo:
  pessoa = json.load(arquivo)

print(pessoa)




