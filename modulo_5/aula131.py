# @property - um getter no modo Pythônico
# getter - um método para obter um atributo
# cor -> get_cor()
# modo pythônico - modo do Python de fazer coisas
# @property é uma propriedade do objeto, ela
# é um método que se comporta como um
# atributo 🤯 🤯 🤯
# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código


class Caneta:
  def __init__(self, cor):
    self.cor_tinta = cor

  @property
  def cor(self):
    return f'Caneta {self.cor_tinta}, {self.cor_tinta} caneta\nCaneta {self.cor_tinta} ta marcada com a minha letra...'

caneta_azul = Caneta('Azul')
print(caneta_azul.cor)