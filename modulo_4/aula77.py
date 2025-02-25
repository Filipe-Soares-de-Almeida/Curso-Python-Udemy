# Exercicios - sistema de perguntas e respostas

perguntas = [
  {
    'Pergunta': 'Quanto é 2+2?',
    'Opções': ['1', '3', '4', '5'],
    'Resposta': '4'
  },
  { 
    'Pergunta': 'Quanto é 5*5?',
    'Opções': ['25', '55', '10', '51'],
    'Resposta': '25'
  },
  {
    'Pergunta': 'Quanto é 10/2?',
    'Opções': ['4', '5', '2', '1'],
    'Resposta': '5'
  }
]

def jogar():
  respostas_certas = 0

  def verifica_resposta(resposta_correta):
    if resposta_correta:
      return 'Ta on fire pae! 🔥\n', 1
    
    return 'Ae não paezão! 😞\n', 0


  for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta']);

    opcoes_lista = pergunta['Opções'];

    opcoes_escolha = ''
    for i, opcao in enumerate(opcoes_lista):
      opcoes_escolha += f'{i}) {opcao}\n'

    print(opcoes_escolha)

    escolha = int(input('Escolha uma opção: '))
    resultado, contador = verifica_resposta(opcoes_lista[escolha] == pergunta['Resposta'])
    print(resultado)
    respostas_certas += contador

  else:
    texto = 'Parabens'
    if respostas_certas == 0:
      texto = 'Que pena'

    print(f'{texto}, você acertou {respostas_certas} de {len(perguntas)} perguntas.')
    

  
jogar()