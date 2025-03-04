"""
Funções decoradoras e decoradores em python (decorators)
Decorar = Adicionar / Remover / Restringir / Alterar
Decoradores são usados para fazer o python usar funções
decoradas em outras funções
decoradores são "Syntax sugar"
"""
def criar_funcao(func):
  def interno(*args, **kwargs):
     for arg in args:
       string_valido(arg)
        
     return func(*args, **kwargs)

  return interno

@criar_funcao
def inverte_string(string):
  return string[::-1]  


def string_valido(param):
  if not isinstance(param, str):
    raise TypeError('Argumento inválido, param deve ser uma string')


# invertido_checando = criar_funcao(inverte_string)

invertido = inverte_string(123)

print(invertido)