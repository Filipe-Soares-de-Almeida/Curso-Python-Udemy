lista1 = []

for x in range(3):
  for y in range(3):
    lista1.append((x, y))

lista2 = [
  (x, y) 
  for x in range(3) 
  for y in range(3)
]

lista3 = [
  [x for y in range(3)] 
  for x in range(3) 
  for y in range(3)
]

print(lista3)

