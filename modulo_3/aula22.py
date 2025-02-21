# operadores logicos
# and, or, not
# and = todas as condicoes precisam ser verdadeiras
# or = pelo menos uma condicao precisa ser verdadeira
# not = inverte o valor da condicao


# sao considerados falsy 
# False, 0, None, empty strings ''


entrada = input("[E]ntrar [S]air: ")
senha_digitada = input("Senha: ") or "Sem senha"

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
  print("Entrar")
else:
  print("Sair")

print(senha_digitada)