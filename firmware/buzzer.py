from machine import Pin, PWM

buzzer = PWM(Pin(27)) #configuro el pin del buzzer como una señal rapida
buzzer.duty(0) #EL buzzer no suena al estar en cero

def sonar(frecuencia):
    buzzer.duty(frecuencia)

def silenciar():
    buzzer.duty(0)