for i in range(10):
  if i == 2:
    print ('i e igual a 2')
    continue
  
  if  i == 8:
    print ('i e igual a 8')
    break
  
  for j in range(10):
    print(i, j)
    
else: 
  print('Finalizou')