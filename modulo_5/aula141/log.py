# Abstração

class Log:
  def _log(self, msg):
    raise NotImplementedError('Implementar o método log')
  
  def log_error(self, msg):
    return self._log(f'ERRO: {msg}') 
  
  def log_success(self, msg):
    return self._log(f'SUCESSO: {msg}')

class LogFileMixin(Log):
  def _log(self, msg):
    print(msg)
  
class LogPrintMixin(Log):
  def _log(self, msg):
    print(f'{msg} - {type(self).__name__}')



if __name__ == '__main__':
  l = LogPrintMixin()
  l.log_error('Mensagem')
  l.log_success('Mensagem')