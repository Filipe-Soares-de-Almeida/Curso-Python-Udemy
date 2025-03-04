# groupby - agrupando valores (itertools)
from itertools import groupby

alunos = [
  {'nome': 'João', 'nota': 'A'},
  {'nome': 'Maria', 'nota': 'B'},
  {'nome': 'Pedro', 'nota': 'C'},
  {'nome': 'Ana', 'nota': 'B'},
  {'nome': 'Carlos', 'nota': 'A'},
  {'nome': 'Lucas', 'nota': 'C'},
  {'nome': 'Mariana', 'nota': 'B'},
  {'nome': 'Fernanda', 'nota': 'A'},
  {'nome': 'Rafael', 'nota': 'C'},
  {'nome': 'Camila', 'nota': 'B'}
]

# test = [1,1,1,1,1, 2, 3, 4]
# grupos = groupby(test)

alunos_agrupados = sorted(alunos, key=lambda aluno: aluno['nota'])

grupos = groupby(alunos_agrupados, key=lambda aluno: aluno['nota'])

for chave, grupo in grupos:
  print(chave, *list(grupo), sep='\n')