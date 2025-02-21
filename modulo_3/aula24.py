# Operadores in e not in
# in - verifica se um elemento esta na sequencia
# not in - verifica se um elemento nao esta na sequencia
#  0 1 2 3 4 5
#  m a c a c o 
# -6-5-4-3-2-1

# nome = 'Macaco'

# print(nome[3])
# print(nome[-5])


# print('M' in nome)
# print('d' in nome)


nome = input('Digite um nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
  print(f'{encontrar} foi encontrado em {nome}')  
else:
  print(f'{encontrar} nao foi encontrado em {nome}')