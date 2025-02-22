"""
CPF: 746824890-70

Colete a soma dos 9 primeiros digitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva comecando de 10

Ex.:  746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0
    70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisao da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
  o resultado é 0
contrario disso:
  o resultado é o valor da conta


O primeiro digito do CPF é 7
"""


cpf = '972.080.520-00'
cpf = cpf.replace('.', '').replace('-', '')

cpf_digitos = cpf[:9]
lista_somas = []

range_cpf = range(10, 1, -1)
for i, peso in enumerate(range_cpf):
  lista_somas.append(int(cpf_digitos[i]) * peso)

soma = 0
for valor in lista_somas:
  soma += valor

multiplicacao = soma * 10
resto = multiplicacao % 11

digito_1 = 0 if resto > 9 else resto

print(f'Primeiro digito: {digito_1}')

