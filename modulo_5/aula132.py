# @property + @setter - getter e setter no modo Pythônico
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Atributos que começar com um ou dois underlines
# não devem ser usados fora da classe.
#  🐍🤓🤯🤯🤯🤯

class Caneta:
  def __init__(self, cor = None):
    self.cor = cor
  @property
  def cor(self):
    return f'Caneta {self.__cor}, {self.__cor} caneta\nCaneta {self.__cor} ta marcada com a minha letra...'
  
  @cor.setter
  def cor(self, valor):
    if valor.capitalize != 'Azul':
      raise ValueError('Nesta casa aceitamos apenas caneta azul. azul caneta')
    
    self.__cor = valor


caneta_azul = Caneta('Azul')
print(caneta_azul.cor)

print()

caneta_vermelha = Caneta('Vermelha') 
print(caneta_vermelha.cor)
