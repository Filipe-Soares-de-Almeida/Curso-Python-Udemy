"""
Faça uma lista de compras com listas
O usuario deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de indices inexistentes na lista
"""
import os

lista_de_compras = []
while True:
  acao_usuario = input('Selecione uma opção\n [I]nserir [A]pagar [L]istar: ').upper()
  os.system('clear')  
  if acao_usuario.startswith('I'):
    item = input('Item a ser adicionado: ')
    lista_de_compras.append(item)
  elif acao_usuario.startswith('A'):
    try:
      del lista_de_compras[int(input('Indice do Item a ser removido: '))]
    except (IndexError, ValueError):
      print('Não foi possivel apagar este indice') 
  elif acao_usuario.startswith('L'):
    if len(lista_de_compras) == 0:
      print('Nada para listar')
      continue
    
    for i, item in enumerate(lista_de_compras):
      print(i, item)