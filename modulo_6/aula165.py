# Exercício solucionado: calculando as datas e parcelas de um empréstimo
# Maria pegou um empréstimo de 1.000.000
# para realizar o pagamento em 5 anos.
# A data em que ela pegou o empréstimo foi
# 20/12/2020 e o vencimento de cada parcela
# é no dia 20 de cada mês.
# - Crie a data do empréstimo
# - Crie a data do final do empréstimo
# - Mostre todas as datas de vencimento e o valor de cada parcela
from datetime import datetime
from dateutil.relativedelta import relativedelta

# ANOS_PARCELA = 5
# MESES_PARCELA = ANOS_PARCELA * 12
# VALOR_EMPRESTIMO = 1_000_000
# VALOR_PARCELA = round(VALOR_EMPRESTIMO / MESES_PARCELA, 2)

# data_emprestimo = datetime(year=2020, month=12, day=20)
# data_final_emprestimo = data_emprestimo + relativedelta(years=ANOS_PARCELA)


# print(f'Data do emprestimo: {data_emprestimo}')
# print(f'Data final do emprestimo: {data_final_emprestimo}')
# print()

# data_parcela = data_emprestimo

# mes_parcela = 1
# while mes_parcela <= MESES_PARCELA:
#   data_parcela += relativedelta(months=1)
#   print(f'Parcela: {mes_parcela}/{MESES_PARCELA}')
#   print(f'Data do vencimento: {data_parcela.strftime("%Y/%m/%d")}')
#   print(f'Valor da parcela: {VALOR_PARCELA}')
#   print()
#   mes_parcela += 1


valor_total = 1_000_000
data_emprestimo = datetime(year=2020, month=12, day=20)
delta_anos = relativedelta(years=5)
data_final = data_emprestimo + delta_anos


data_parcelas = []
data_parcela = data_emprestimo
while data_parcela < data_final:
  data_parcelas.append(data_parcela)

  data_parcela += relativedelta(months=1)


num_parcelas = len(data_parcelas)
valor_parcela = round(valor_total / num_parcelas, 2)
for data in data_parcelas:
  print(f'Parcela {data_parcelas.index(data) + 1}/{num_parcelas}')
  print(data.strftime('%d/%m/%Y'))
  print(f'Valor da parcela: R${valor_parcela:,.2f}')
