"""
Modo de importar módulos em Python

Em Python, há várias maneiras de importar módulos. Abaixo estão listadas todas elas com suas vantagens e desvantagens:
"""

"""
1. Importando todo o módulo:
	* import nome_do_modulo

Vantagem: Permite acesso a todas as funções e variáveis do módulo.
Desvantagem: Pode causar poluição no namespace.
"""

# Exemplo:
import math

"""
2. Importando somente uma função ou variável do módulo:
	* from nome_do_modulo import nome_da_funcao_ou_variavel

Vantagem: Permite acesso apenas às funções e variáveis necessárias, evitando poluição no namespace.
Desvantagem: Pode ser necessário importar várias funções ou variáveis separadamente.
"""

# Exemplo:
from math import sin

"""
3. Importando todas as funções e variáveis do módulo:
	* from nome_do_modulo import *

Vantagem: Permite acesso a todas as funções e variáveis do módulo sem ter que importar cada uma separadamente.
Desvantagem: Pode causar poluição no namespace e pode ser difícil de manter a ordem das importações.
"""

#Exemplo:
from math import *

"""
4. Importando um módulo com um nome diferente:
	* import nome_do_modulo as outro_nome

Vantagem: Permite importar um módulo com um nome mais curto ou mais fácil de lembrar.
Desvantagem: Pode causar confusão se o nome não for único.
"""

#Exemplo:
import math as m

"""
5. Importando um módulo que esta em um pacote:
	* from nome_do_pacote.nome_do_modulo import nome_da_funcao_ou_variavel

Vantagem: Permite importar módulos que estão em pacotes sem ter que importar todo o pacote.
Desvantagem: Pode ser necessário importar vários módulos separadamente.
"""

# Exemplo:
from pandas.api import extensions
"""

6. Importando um módulo que esta em um pacote com um nome diferente:
	* from nome_do_pacote import nome_do_modulo as outro_nome

Vantagem: Permite importar um módulo que está em um pacote com um nome mais curto ou mais fácil de lembrar.
Desvantagem: Pode causar confusão se o nome não for único.
"""

# Exemplo:
from pandas import api as m

"""
7. Importando um módulo relativo:
	* from .nome_do_modulo import nome_da_funcao_ou_variavel

Vantagem: Permite importar módulos que estão no mesmo pacote sem ter que importar todo o pacote.
Desvantagem: Pode ser necessário importar vários módulos separadamente.
"""

# Exemplo:
from .aula95 import soma

"""
8. Importando um módulo relativo com um nome diferente:
	* from .nome_do_modulo import nome_da_funcao_ou_variavel as outro_nome

Vantagem: Permite importar um módulo que está no mesmo pacote com um nome mais curto ou mais fácil de lembrar.
Desvantagem: Pode causar confusão se o nome não for único.
"""
# Exemplo:
from .aula95 import soma as s
