"""
Faça um programa que peça ao usuário para digitar um numero inteiro,
informe se este numero é par ou impar. Caso o usuário não digite um numero inteiro, 
informe que não é um numero inteiro.
"""

num = input('Digite um numero inteiro: ')
try:
  num = int(num)
  
  if num % 2 == 0:
    print(f'O numero {num} é par!')
  else:
    print(f'O numero {num} é impar!')
    
except:
  print('Isso nao e um numero inteiro!') 


"""
Faça um programa que pergunte a hora ao usuário e, 
baseando-se no horário descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
# horario = input('Digite o horário (numero inteiro): ')

# try:
#   horario = int(horario)
  
#   if horario >= 0 and horario <= 11:
#     print('Bom dia!')
#   elif horario >= 12 and horario <= 17:
#     print('Boa tarde!')
#   elif horario >= 18 and horario <= 23:
#     print('Boa noite!')
#   else:
#     print('Isso nao e um horário valido!')
# except:
#   print('Isso nao e um horário valido!')



# """
# Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreva "Seu nome é curto";
# se tiver entre 5 e 6 letras, escreva "Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande"
# """
# nome = input('Digite o seu nome: ')
# tamanho_nome = len(nome)

# if tamanho_nome <= 4:
#   print('Seu nome é curto!')
# elif tamanho_nome in [5, 6]:
#   print('Seu nome é normal!')
# else:
#   print('Seu nome é muito grande!')
