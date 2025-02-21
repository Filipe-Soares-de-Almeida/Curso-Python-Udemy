"""
Introdução ao desempacotamento
"""

nome1, nome2, nome3 = ["Maria", "Helena", "Luiz"]
print(nome1, nome2, nome3)


# empacotar o resto das variaveis em uma só
nome1, *_ = ["Maria", "Helena", "Luiz"]
print(nome1, resto)