"""
Exercicio - Salve sua classe em JSON
Salve os dados da sua classe em JSON e depois crie novamente as instancias da classe com os dados salvos
Faça em arquivos separados.

"""
import json


class Pessoa:
  def __init__(self, nome, sobrenome, idade, altura, peso, enderecos=None):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade
    self.altura = altura
    self.peso = peso
    self.enderecos = enderecos if enderecos is not None else []



p1 = Pessoa(
  'Joao', 
  'da Bananeira', 
  20, 
  1.80, 
  80,
  [ {'rua': 'Rua 1', 'numero': 123},
    {'rua': 'Rua 2', 'numero': 456},
  ]
)

p2 = Pessoa(
  'Zezim', 
  'do Pe Sujo', 
  25, 
  1.90, 
  90,
  [ {'rua': 'Rua 4', 'numero': 789},
    {'rua': 'Rua 5', 'numero': 1011},
  ]
)

dados_p1 = vars(p1)
dados_p2 = vars(p2)

def salvar(dados, nome_arquivo):
  with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(dados, arquivo, indent=2, ensure_ascii=False)

  print(f'Dados salvos no arquivo {nome_arquivo} com sucesso!')

def carregar(nome_arquivo):
  with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
    dados = json.load(arquivo)

  print(f'Dados carregados do arquivo {nome_arquivo} com sucesso!')
  return dados

salvar(dados_p1, 'aula127_a.json')
salvar(dados_p2, 'aula127_b.json')

pessoa1 = Pessoa(**carregar('aula127_a.json'))
pessoa2 = Pessoa(**carregar('aula127_b.json'))

print('Pessoa1:')
print(vars(pessoa1))

print('Pessoa2:')
print(vars(pessoa2))