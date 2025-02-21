"""
Faça um jogo para o usuario adivinhar qual a palavra secreta.

- Voce vai propor uma palavra secreta qualquer  e vai dar a possibilidade
para o usuario digitar apenas uma letra.

- Quando o usuario digitar uma letra, voce vai conferir se a letra digitada está na palavra secreta.
  - Se a letra digitada estiver na palavra secreta; exiba a letra;
  - Se a letra digitada não estiver na palavra secreta; exiba *.
Faça uma contagem de tentativas do seu usuário
"""


palavra_secreta = 'Pneumoultramicroscopicossilicovulcanoconiose'
palavra_secreta_visivel = '*' * len(palavra_secreta)

tentativas = 0
while palavra_secreta_visivel != palavra_secreta:
  tentativas += 1
  letra = input('Digite uma letra: ')
  if not letra:
    print('Digite uma letra!')
    continue
  elif len(letra) > 1:
    print('Digite apenas uma letra!')
    continue
  
  if letra in palavra_secreta.lower():
    i = 0
    while i < len(palavra_secreta):
      if palavra_secreta[i].lower() == letra:
        palavra_secreta_visivel = palavra_secreta_visivel[:i] + palavra_secreta[i] + palavra_secreta_visivel[i + 1:]
      i += 1
      
    print(palavra_secreta_visivel)
  else:
    print(palavra_secreta_visivel)
else: 
  print(f'Parabens, voce adivinhou a palavra secreta! a palavra era: {palavra_secreta} ({tentativas} tentativas)')

