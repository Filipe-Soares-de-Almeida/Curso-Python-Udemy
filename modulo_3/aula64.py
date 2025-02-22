import random

digitos = ''

for i in range(9):
  digitos += str(random.randint(0, 9))

cpf = digitos
cpf = cpf.replace('.', '').replace('-', '')

cpf_digitos = cpf[:9]
lista_somas = []

range_cpf = range(10, 1, -1)
for i, peso in enumerate(range_cpf):
  lista_somas.append(int(cpf_digitos[i]) * peso)

soma = 0
for valor in lista_somas:
  soma += valor

# multiplicacao = soma * 10
# resto = multiplicacao % 11

# digito_1 = 0 if resto > 9 else resto

resto = soma % 11

digito_1 = 0 if resto < 2 else 11 - resto

print(f'Primeiro digito: {digito_1}')

cpf_digitos = cpf[:9] + str(digito_1)
lista_somas = []

range_cpf = range(11, 1, -1)
for i, peso in enumerate(range_cpf):
  lista_somas.append(int(cpf_digitos[i]) * peso)

soma = 0
for valor in lista_somas:
  soma += valor

# multiplicacao = soma * 10
resto = soma % 11

digito_2 = 0 if resto < 2 else 11 - resto


print(f'{cpf_digitos}{digito_2}')

# print(f'Segundo digito: {digito_2}')

# cpf_digitos = cpf[:9] + str(digito_1) + str(digito_2)

# print('CPF Valido' if cpf_digitos == cpf else 'CPF Invalido')