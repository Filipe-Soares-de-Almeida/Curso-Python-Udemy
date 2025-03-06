# Métodos em instancias de classes Python

class Carro:
  def __init__(self, nome, ano, cor):
    self.nome = nome
    self.ano = ano
    self.cor = cor

  def ligar(self):
    if self.cor == 'Azul' and self.nome == 'Fusca':
      print('FUSCA AZULLLLL 🤜🤜🤜🤜')

    print(f'{self.nome} ligou\n')
    print

  def desligar(self):
    print(f'{self.nome} desligou\n')

  def acelerar(self):
    for i in range(0, 100, 10):
      print(f'{self.nome} está a {i} km/h')
      
      if i >= 50 and self.nome == 'Marea Turbo':
        print(f'{self.nome} pegou fogo 🔥🔥🔥')
        break
    
  def informacoes(self):
    print(f'Nome: {self.nome}')
    print(f'Ano: {self.ano}')
    print(f'Cor: {self.cor}')
    print()

fusca = Carro('Fusca', 1970, 'Azul')
celta = Carro('Celta', 2010, 'Branco')
marea_turbo = Carro('Marea Turbo', 2015, 'Prata')

fusca.informacoes()
fusca.ligar()
fusca.acelerar()
fusca.desligar()

celta.informacoes()
celta.ligar()
celta.acelerar()
celta.desligar()

marea_turbo.informacoes()
marea_turbo.ligar()
marea_turbo.acelerar()
marea_turbo.desligar()