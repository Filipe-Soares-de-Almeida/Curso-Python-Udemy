# Criando datas com módulo datetime
# datetime(ano, mês, dia)
# datetime(ano, mês, dia, horas, minutos, segundos)
# datetime.strptime('DATA', 'FORMATO')
# datetime.now()
# https://pt.wikipedia.org/wiki/Era_Unix
# datetime.fromtimestamp(Unix Timestamp)
# https://docs.python.org/3/library/datetime.html
# Para timezones
# https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
# Instalando o pytz
# pip install pytz types-pytz
from datetime import datetime

DATA_STR_DATA = '2022/04/20 07:49:23'
DATA_STR_DATA = '20/04/2022'
DATA_STR_FMT = '%d/%m/%Y'

# data = datetime(2022, 4, 20, 7, 49, 23)
data = datetime.strptime(DATA_STR_DATA, DATA_STR_FMT)
print(data)
