"""
CONSTANTE = 'Variavel que nunca muda'
"""

velocidade = 61 # velocidade atual do carro
local_carro = 100 # local em que o carro esta na estrada


RADAR_1 = 60 # velocidade maxima do radar 1
LOCAL_1 = 100 # local onde o radar 1 está
RADAR_RANGE = 1 # a distancia onde o radar pega

vel_carro_pass_radar_1 = velocidade > RADAR_1
carro_passou_radar_1 = local_carro >= (LOCAL_1 - RADAR_RANGE) \
  and  local_carro <= (LOCAL_1 + RADAR_RANGE)
carro_multado = vel_carro_pass_radar_1 and carro_passou_radar_1;



if vel_carro_pass_radar_1:
  print("Velocidade maior que o permitido")
  
if carro_passou_radar_1:
  print("Carro passou no radar 1")
  
if carro_multado:
  print("Carro multado no radar 1")