"""
Iterando strings com while
"""
nome = 'Pneumoultramicroscopicossilicovulcanoconiose'
nome_com_asterisco = '';

letra = 0
while letra < len(nome):
  nome_com_asterisco += '*' + nome[letra] 
  letra += 1
  
  
print(nome_com_asterisco)