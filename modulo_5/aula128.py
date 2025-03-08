"""
Metodos de classe + factories (fabricas)

São metodos onde  "self" será "cls", ou seja,
ao inves de receber a instancia no primeiro parametro,
receberemos a classe.
"""


class Pessoa:
  ano = 2025

  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade

  @classmethod
  def metodo_de_classe(cls):
    print(f'Ano atual: {cls.ano}')

print(Pessoa.metodo_de_classe())