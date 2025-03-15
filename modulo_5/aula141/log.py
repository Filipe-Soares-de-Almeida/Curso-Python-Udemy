# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'
class Log:
  def _log(self, msg):
    raise NotImplementedError('Implementar o método log')
  
  def log_error(self, msg):
    return self._log(f'ERRO: {msg}') 
  
  def log_success(self, msg):
    return self._log(f'SUCESSO: {msg}')

class LogFileMixin(Log):
  def _log(self, msg):
    msg_formatada = f'{msg} - {type(self).__name__}'
    print('Salvando')
    with open(LOG_FILE, 'a', encoding='utf-8') as arquivo:
      arquivo.write(msg_formatada)
      arquivo.write('\n')
  
class LogPrintMixin(Log):
  def _log(self, msg):
    print(f'{msg} - {type(self).__name__}')

if __name__ == '__main__':
  lp = LogPrintMixin()
  lp.log_error('erro print')
  lp.log_success('sucesso print')

  lf = LogFileMixin()
  lf.log_error('erro file')
  lf.log_success('sucesso file')  