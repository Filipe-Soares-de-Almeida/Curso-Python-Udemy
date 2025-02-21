nome = 'Tatupeba'
altura = 0.95
peso = 6.5
imc = peso / (altura ** 2) # IMC = peso / (altura * altura)

linha_1 = f'{nome} tem {altura:.2f} de altura,'
linha_2 = f'pesa {peso:.2f} quilos e seu imc é'
linha_3 = f'{imc:.2f}'

print(linha_1)
print(linha_2)
print(linha_3)