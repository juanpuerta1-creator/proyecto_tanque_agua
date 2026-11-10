from machine import Pin

led_rojo = Pin(32, Pin.OUT) #Pin de salida al ser un led
led_amarillo = Pin(33, Pin.OUT)
led_verde = Pin(25, Pin.OUT)

def encender_ledverde():
    led_verde.value(1)
    led_amarillo.value(0)
    led_rojo.value(0)

def encender_ledamarillo():
    led_verde.value(0)
    led_amarillo.value(1)
    led_rojo.value(0)

def encender_ledrojo():
    led_verde.value(0)
    led_amarillo.value(0)
    led_rojo.value(1)

def apagar_leds():
    led_verde.value(0)
    led_amarillo.value(0)
    led_rojo.value(0)