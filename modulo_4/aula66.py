"""
Argumentos nomeados e não nomeados em funções Python
Argumentos nomeados tem nome com sinal de igual
Argumentos não nomeados recebe apenas o argumento (valor)
"""

def soma(num1, num2):
    print(num1 + num2)


soma(200, 300)

soma(num2=200, num1=300)