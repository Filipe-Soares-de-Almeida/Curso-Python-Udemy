"""
@staticmethod (métodos estáticos) são inúteis em Python =)
Métodos estáticos são métodos que estão dentro da classe, mas não tem acesso ao self nem ao cls.
Em resumo, são funções que existem dentro da sua classe.
"""

class Pessoa:
    @staticmethod
    def dizer_oi():
        print('Oi')

Pessoa.dizer_oi()
