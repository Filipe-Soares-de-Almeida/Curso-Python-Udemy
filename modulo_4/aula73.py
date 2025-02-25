"""
Higher Order Functions

Higher Order Functions são funções que podem ser usadas como argumentos em outras funções, 
ou podem ser retornadas por outras funções. 
Isso permite criar funções mais dinamicas e flexiveis, 
pois podem ser usadas em diferentes contextos.
"""

def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)

v = executa(saudacao, 'Bom dia', 'Joao')

print(v)
