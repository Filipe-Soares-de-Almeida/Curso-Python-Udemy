"""
Funções recursivas e recursão em python (recursion)
- Funções que podem se chamar de volta
- uteis p/ divisão de problemas

Toda função recursiva deve ter
- Um problema que possa ser dividido em partes menores
- Um caso recursivo
- um caso base que para a recursão
- fatorial - n! = 5 * 4 * 3 * 2 * 1 = 120

- Vantagens:
  - Divisão de problemas complexos em problemas menores
  - Melhor compreensão e manutenção do código
  - Menos linha de código
- Desvantagens:
  - Perfomance piora devido ao uso excessivo de memória
  - Se a recursão for muito profunda, pode causar um erro (StackOverflowError)
"""

def fatorial(n):
  # caso base
  # se n for 0 ou 1, a função deve retornar 1
  # pois o fatorial de 0 e 1 é 1
  if n <= 1:
    return 1
  else:
    # caso recursivo
    # a função chama ela mesma com o valor de n - 1
    # e multiplica o resultado com o valor atual de n
    # isso vai criar uma "pilha" de chamadas recursivas
    # ate que o caso base seja alcançado
    return n * fatorial(n - 1)

res = fatorial(120)

# print(type(res), res)  


def recursivo(start=0, end=10):  
  if start < end:
    print(start)
    return recursivo(start + 1, end)
  
  print(f'{start=}')


recursivo()