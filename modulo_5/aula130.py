"""
method vs @classmethod vs @staticmethod

method -> self, metodo de instancia
@classmethod -> cls, metodo de classe
@staticmethod -> metodo estatico (❌self, ❌cls)
"""

class Connection:
  def __init__(self, host='localhost'):
    self.host = host
    self.user = None
    self.password = None

  def set_user(self, user):
    self.user = user

  def set_password(self, password):
    self.password = password

  @classmethod
  def create_with_auth(cls, user, password):
    connection = cls()
    connection.set_user(user)
    connection.set_password(password)
    return connection
  
  @staticmethod
  def soma(x, y):
    return x + y


c1 = Connection()

c1.set_user('admin')
c1.set_password('123456')

print(c1.user)
print(c1.password)