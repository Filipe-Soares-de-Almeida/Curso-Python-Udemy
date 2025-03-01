# generator expression, Iterables e Iterators em Python
import sys

iterable = ['Eu', 'Tenho', '__iter__']

iterator = iterable.__iter__()

lista = [n for n in range(10000000)]
generator = (n for n in range(1000000000))

print(sys.getsizeof(lista))
print(sys.getsizeof(generator))


for n in generator:
  print(n)