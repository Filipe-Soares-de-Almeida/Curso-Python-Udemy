# Funções decoradas e decoradores com metodos

def add_repr(cls):
  def inner_repr(self):
    return f'{type(self).__name__}({self.__dict__})'
  cls.__repr__ = inner_repr
  return cls

def meu_planeta(metodo):
  def inner_metodo(self, *args, **kwargs):
    return metodo(self, *args, **kwargs)
  return inner_metodo


@add_repr
class Time:
  def __init__(self, nome):
    self.nome = nome

@add_repr
class Planeta:
  def __init__(self, nome):
    self.nome = nome

  @meu_planeta
  def falar_nome(self):
    return f'Eu sou o planeta {self.nome}'

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)

print(terra.falar_nome())
print(marte.falar_nome())