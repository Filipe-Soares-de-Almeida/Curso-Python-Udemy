from log import LogPrintMixin

class Eletronico:
  def __init__(self, nome):
    self.nome = nome
    self._ligado = False
    
  def ligar(self):
    if not self._ligado:
      self._ligado = True

  def desligar(self):
    if self._ligado:
      self._ligado = False


class Smartphone(Eletronico, LogPrintMixin):
  def ligar(self):
    super().ligar()

    self.log_success(f'{self.nome} ligou!')

  def desligar(self):
    super().desligar()

    self.log_error(f'{self.nome} desligou!')