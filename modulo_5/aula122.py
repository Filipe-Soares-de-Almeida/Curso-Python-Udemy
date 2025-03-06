# Métodos em instancias de classes Python

class Carro:
  def __init__(self, nome, ano, cor, motor, combustivel):
      self.nome = nome
      self.ano = ano
      self.cor = cor
      self.motor = motor
      self.combustivel = combustivel
      print(f'{self.nome} criado com sucesso!')

  def ligar(self):
    if self.cor == 'Azul' and self.nome == 'Fusca':
      print('FUSCA AZULLLLL 🤜🤜🤜🤜')

    print(f'{self.nome} ligou\n')

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
    print(f'Motor: {self.motor}')
    print(f'Combustível: {self.combustivel}')
    print()

fusca = Carro('Fusca', 1970, 'Azul', '1.6', 'Gasolina')
celta = Carro('Celta', 2010, 'Branco', '1.0', 'Flex')
marea_turbo = Carro('Marea Turbo', 2015, 'Prata', '2.0 Turbo', 'Gasolina')

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
