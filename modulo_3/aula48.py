"""
Listas em Python

Tipo list - Mutável
Suporta vários valores de qualquer tipo
conhecimentos reutilzáveis - indexação e fatiamento de listas
Metodos uteis: append, insert, pop, del, clear, extend,+
"""


# string = 'abcde' # = 5 caracteres
# lista = [123, True, 'texto', 1.2, []]
# print(lista)

# lista = [10, 20, 30, 40]
# lista[2] = 500

# # deletar
# del lista[2]
# print(lista)
# # adicionar 
# lista.append(50)
# print(lista)

# # pop - remover ultimo
# lista.pop()
# print(lista)


# lista = [10, 20, 30, 40]
# lista.insert(0, 100)
# print(lista)


# lista_1 = [10, 20, 30, 40]
# lista_2 = [50, 60]
# lista_c = lista_1 + lista_2;
# lista_1.extend(lista_2)
# print(lista_c)
# print(lista_1)


# lista mutavel aponta para o mesmo endereço de memoria
# usar copy para criar uma copia de uma lista
l1 = ['foo', 'bar']
l2 = l1

l1[0] = 'baz'
print(l2)