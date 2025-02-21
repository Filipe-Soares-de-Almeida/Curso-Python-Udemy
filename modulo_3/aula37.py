contador = 0;
while contador < 100:
  contador += 1
  
  if contador % 2 != 0:
    continue;
  
  print(contador)
  
  if contador >= 50:
    print("Chegou em 50")
    break;
  
  
print("Acabou")