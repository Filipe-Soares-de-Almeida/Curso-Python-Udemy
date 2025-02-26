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

  def verifica_resposta(resposta_usuario, resposta_correta):
    resultado = 'Ae não paezão! 😞\n', 0

    try:
      resposta_usuario = int(resposta_usuario)
 
      if opcoes_lista[resposta_usuario] == resposta_correta:
        resultado = 'Ta on fire pae! 🔥\n', 1
      
    except:
      return resultado
    
    return resultado
        

  for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta']);

    opcoes_lista = pergunta['Opções'];

    opcoes_escolha = ''
    for i, opcao in enumerate(opcoes_lista):
      opcoes_escolha += f'{i}) {opcao}\n'

    print(opcoes_escolha)

    resultado, contador = verifica_resposta(input('Escolha uma opção: '), pergunta['Resposta'])
    print(resultado)
    respostas_certas += contador

  else:
    texto = 'Parabens'
    if respostas_certas == 0:
      texto = 'Que pena'

    print(f'{texto}, você acertou {respostas_certas} de {len(perguntas)} perguntas.')
    

  
jogar()