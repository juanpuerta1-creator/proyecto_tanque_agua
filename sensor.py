from machine import Pin, time_pulse_us
from time import sleep

Altura_Tanque = 100
Nivel_Min = 20 #Nivel minimo del agua
Nivel_Max = 90 #Nivel maximo del agua


trig = Pin(19, Pin.OUT) #pin de salida
echo = Pin(18, Pin.IN) #pin de entrada

def medir_distancia():
  trig.value(0)
  sleep(1)
  trig.value(1)
  sleep(1)
  trig.value(0)

  tiempo = time_pulse_us(echo, 1, 30000)

  if tiempo > 0:
    distancia = (tiempo * 0.0343) / 2
    return distancia

def medir_nivel():
  distancia = medir_distancia()

  nivel_agua = (Altura_Tanque - distancia) / Altura_Tanque * 100

  if nivel_agua < 0:
    nivel_agua = 0
  if nivel_agua > 100:
    nivel_agua = 100

  return nivel_agua