# Exemplo de como usar public, protected e private em Python

from functools import partial

class Pessoa:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self._idade = idade
        self.__cpf = cpf

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, idade):
        if idade < 0:
            raise ValueError("idade não pode ser negativa")
        self._idade = idade

    @property
    def cpf(self):
        return self.__cpf

    @cpf.setter
    def cpf(self, cpf):
        self.__cpf = cpf

pessoa = Pessoa("Joao", "123456789", 25)

print(pessoa.nome)
print(pessoa.cpf)
print(pessoa.idade)