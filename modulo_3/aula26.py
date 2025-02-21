# formatação basica de strings
# s - string
# d e i - int
# f - float
# x e X - hex
# (caractere)(><^)(quantidade)
# > - esquerda
# < - direita
# ^ - centraliza
# Sinal - + ou -

# Ex: 0>-100,2f
# Conversion flags - !r !s !a

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #PADL
print(f'{variavel: <10}')


print(f'{1000.9591238:.1f}')

