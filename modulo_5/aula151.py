# Funções decoradas e decoradores com classes

def add_repr(cls):
  def inner_repr(self):
    return f'{type(self).__name__}({self.__dict__})'
  cls.__repr__ = inner_repr
  return cls


@add_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

@add_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome

brasil = Time('Brasil')
portugal = Time('Portugal')

terra = Planeta('Terra')
marte = Planeta('Marte')

print(brasil)
print(portugal)

print(terra)
print(marte)