"""
Exercício - Lista de tarefas com desfazer e refazer
todo     => [ ]                        -> lista de tarefas
todo     => ['fazer café']             -> Adicionar fazer café
todo     => ['fazer café', 'caminhar'] -> Adicionar caminhar
desfazer => ['fazer café',]            -> Refazer ['caminhar'] 
desfazer => [ ]                        -> Refazer ['caminhar', 'fazer café']
refazer  => todo ['fazer café']
refazer  => todo ['fazer café', 'caminhar']
"""
import os

def executa_acao(*args, **kwargs):
  acao = kwargs['acao_usuario']
  
  if acao == 'listar':
    return listar(**kwargs)
  
  if acao == 'desfazer':
    return desfazer(**kwargs)
  
  if acao == 'refazer':
    return refazer(**kwargs)
  
  if acao == 'clear':
    return clear()

  adiciona_tarefa(**kwargs)
  

def listar(*args, **kwargs):
  print('TAREFAS')
  print()
  for tarefa in kwargs['lista_principal']:
    print('-', tarefa)
  print()

def desfazer(*args, **kwargs):
  if not kwargs['lista_principal']:
    print('Nada para desfazer\n')
    return
  
  tarefa = kwargs['lista_principal'].pop()
  kwargs['lista_refazer'].append(tarefa)
  listar(**kwargs)

def refazer(*args, **kwargs):
  if not kwargs['lista_refazer']:
    print('Nada para refazer\n')
    return
  tarefa = kwargs['lista_refazer'].pop()
  kwargs['lista_principal'].append(tarefa)
  listar(**kwargs)

def adiciona_tarefa(*args, **kwargs):
  kwargs['lista_principal'].append(kwargs['acao_usuario'])
  listar(**kwargs)

def clear():
  os.system('clear')

def funcao_principal():
  lista_principal = []
  # lista_desfazer = []
  lista_refazer = []   
 
  while True:
    print('Comandos: listar, desfazer, refazer')
    acao = input('Digite uma tarefa ou comando: ').lower()
    print()

    argumentos = {
      'acao_usuario': acao,
      'lista_principal': lista_principal,
      # 'lista_desfazer': lista_desfazer,
      'lista_refazer': lista_refazer
    }
    executa_acao(**argumentos)
  

funcao_principal()