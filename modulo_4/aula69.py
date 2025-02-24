"""
Escopo de funções em Python

Escopo significa o local onde aquele codigo pode atingir.
Existe o escopo global e o local.
O escopo global é o escopo onde todo o codigo é alcançável.
O escopo local é o escopo onde o codigo so pode ser atingido quando estiver dentro do bloco que o contem.
"""

x = 1

def meu_escopo_local():
  x = 10 # escopo local
  print("Escopo local: ", x)

meu_escopo_local()
print("Escopo global: ", x) # vai dar erro pois x nao esta disponivel no escopo global



x = 100 # escopo global

def meu_escopo_local():
  """
  Incrementa o valor de x em 1 e o imprime.
  
  O valor de x é global, logo pode ser acessado de qualquer lugar.
  Se o valor de x for alterado em outro lugar, o seu valor aqui 
  tambem será alterado.
  """
  global x # agora x é global
  x += 1 # incrementa o valor de x
  print("Escopo local: ", x)

meu_escopo_local()
print("Escopo global: ", x) # vai printar 101


def funcao_externa():
    """
    Executa uma função interna que imprime uma mensagem na tela.
    
    Essa função serve de exemplo para demonstrar como funciona o escopo de
    variaveis em Python. A função interna está dentro do escopo da função
    externa, logo tem acesso a todas as variaveis da função externa.
    """
    print("Executando função externa", x)
    def funcao_interna():
        print("Executando função interna", x)
    funcao_interna()

funcao_externa()

