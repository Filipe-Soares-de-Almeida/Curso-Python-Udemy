"""
Estrutura de dados Set (Conjunto)

Set é uma estrutura de dados que armazena elementos únicos, sem ordem, sem index, sem chave, sem valor. 
Os elementos em um set são imutáveis, ou seja, não podem ser alterados.

Sets são utilizados para remover elementos duplicados, verificar se um elemento está presente em uma coleção, 
e para realizar operações de união, interseção e diferença entre conjuntos.

Em resumo, um set é uma coleção de elementos únicos, sem ordem, sem index, sem chave, sem valor, e com elementos imutáveis.

Exemplo: {1, 2, 3, 4, 5}

Métodos úteis:

- add(elemento) - Adiciona um elemento ao set
- clear() - Limpa o set
- copy() - Retorna uma cópia do set
- difference(other) - Retorna um novo set com elementos apenas presentes no set atual
- difference_update(other) - Remove de um set os elementos presentes em outro
- discard(elemento) - Remove um elemento do set, se ele existir
- intersection(other) - Retorna um novo set com elementos presentes em ambos os sets
- intersection_update(other) - Atualiza o set atual com a interseção entre ele e outro set
- isdisjoint(other) - Verifica se um set é disjunto de outro (ou seja, se não têm elementos em comum)
- issubset(other) - Verifica se um set é um subconjunto de outro
- issuperset(other) - Verifica se um set é um superconjunto de outro
- pop() - Remove e retorna um elemento aleatório do set
- remove(elemento) - Remove um elemento do set
- symmetric_difference(other) - Retorna um novo set com elementos presentes em um set ou em outro, mas não em ambos
- symmetric_difference_update(other) - Atualiza o set atual com a diferença simétrica entre ele e outro set
- union(other) - Retorna um novo set com todos os elementos de ambos os sets
- update(other) - Atualiza o set atual com a união entre ele e outro set
- | - Union
- & Intersection
"""

# l1 = [1, 2, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5]
# s2 = set(l1)
# l1 = list(s2)

# print(l1)


s1 = {1, 2, 3}
s2 = {2, 3, 4}
s3 = s1 | s2
s3 = s1 & s2
s3 = s1 - s2
s3 = s2 - s1
s3 = s1 ^ s2



print(s3)
