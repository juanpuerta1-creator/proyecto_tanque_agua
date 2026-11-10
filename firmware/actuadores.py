from machine import Pin, PWM

# Bomba

relay = Pin(26, Pin.OUT) #Configuro el relay como una salida.
relay.value(0)

def encender_bomba():
  relay.value(1)

def apagar_bomba():
  relay.value(0)

#Valvula

servomotor = PWM(Pin(2), freq = 50) #configuro el pin como una entrada de pulsos

def mover_servomotor(grados):
  valor = int(26 + (grados / 180) * 102) #a que angulo se debe mover el servomotor
  servomotor.duty(valor)

def abrir_valvula():
  mover_servomotor(90)

def cerrar_valvula():
  mover_servomotor(0)