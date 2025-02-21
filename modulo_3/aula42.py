frase = 'O python é uma linguagem de programação '\
  'multiparadigma. '\
  'Python foi criado por Guido van Rossum.'
  
  


contador = 0 
qtd_repeticoes  = 0
letra_mais_repetida = ''

while contador < len(frase):
    letra = frase[contador].lower()
    qtd = 0
    i = 0
    
    if letra == ' ':
      contador += 1
      continue     
    
    while i < len(frase):
        qtd += frase[i].lower() == letra
        i += 1
        
    if qtd > qtd_repeticoes:
        qtd_repeticoes = qtd
        letra_mais_repetida = letra
    contador += 1

print(f'A letra que mais repetiu foi: {letra_mais_repetida} (Repetiu {qtd_repeticoes} vezes)')  