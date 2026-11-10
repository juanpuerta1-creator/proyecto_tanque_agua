import sensor
import leds
import buzzer

ciclos_maximo = 5

def mostrar_estado(nivel_agua):
    if nivel_agua < sensor.Nivel_Min:
        leds.encender_ledrojo()
        buzzer.sonar(512)
    elif nivel_agua > sensor.Nivel_Min and nivel_agua < sensor.Nivel_Max:
        leds.encender_ledverde()
        buzzer.silenciar()
    else:
        leds.encender_ledamarillo()
        buzzer.sonar(512)