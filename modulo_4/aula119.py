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
import json

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
  
  if acao == 'salvar':
    return salvar_dados(**kwargs)

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

def carregar_dados(*args, **kwargs):
  arquivo = 'aula119.json'
  
  if not os.path.exists(arquivo):
    return

  with open(arquivo, 'r', encoding='utf-8') as arquivo:
    dados_json = json.load(arquivo)
  
  if not dados_json:
    return
  
  kwargs['lista_principal'].extend(dados_json['lista_principal'])
  kwargs['lista_refazer'].extend(dados_json['lista_refazer'])

def salvar_dados(*args, **kwargs):
  arquivo = 'aula119.json'
  
  dados_json = {
    'lista_principal': kwargs['lista_principal'], 
    'lista_refazer': kwargs['lista_refazer']
  }
  
  with open(arquivo, 'w', encoding='utf-8') as arquivo:
    json.dump(dados_json, arquivo, ensure_ascii=False, indent=2)


def funcao_principal():
  lista_principal = []
  lista_refazer = []  

  carregar_dados(lista_principal=lista_principal, lista_refazer=lista_refazer) 
 
  while True:
    print('Comandos: listar, desfazer, refazer, clear, salvar')
    acao = input('Digite uma tarefa ou comando: ').lower()
    print()

    argumentos = {
      'acao_usuario': acao,
      'lista_principal': lista_principal,
      'lista_refazer': lista_refazer
    }
    executa_acao(**argumentos)
  

funcao_principal()