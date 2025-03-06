# Atributos de classe
class Pessoa:
  ano_atual = 2025
  
  def __init__(self, nome, sobrenome, idade):
    self.nome = nome
    self.sobrenome = sobrenome
    self.idade = idade

  def ano_nascimento(self):
    return Pessoa.ano_atual - self.idade

p1 = Pessoa('Joao', 'da Bananeira', 20)
p2 = Pessoa('Zezim', 'do Pé Sujo', 25)

print(p1.ano_nascimento())
print(p2.ano_nascimento())