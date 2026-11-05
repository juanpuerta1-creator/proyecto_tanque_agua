# Control de nivel en un tanque de agua

## Descripción
Elaboración de sistema para medir el nivel de un
tanque de agua, controlar las acciones de la bomba, 
válvulas y alertar cuando el tanque se encuentra 
vacío, por desbordarse o necesita una posible limpieza
luego de cumplir una cantidad especifica de ciclos.
Pensado principalmente para casas.

## Simulación
https://wokwi.com/projects/478704980156509185

## Componentes
| Componentes | Funcion |
| ----------- | ------- |
| ESP32 | Microcontrolador |
| Sensor HC-SR04 | Medir la distancia del agua para conocer el nivel en %|
| Relé | Encender o apagar la bomba |
| Servomotor | Abrir o cerrar la válvula |
| Leds | Conocer estado del tanque visualmente |
| Buzzer | Alarma sonora |

## Funcionalidades

1. Medición del nivel del agua calculando la distancia
2. control automático de la bomba y la válvula.
3. Indicadores con Leds sobre el estado del tanque y buzzer como alarma de advertencia
4. Recomendacion de limpieza del tanque por determinados ciclos.

## Módulos

- **main.py** --> programa principal
- **sensor.py** --> función para medir el nivel del agua
- **leds.py** --> instrucciones para los leds
- **estado.py** --> mostrar estado del tanque de manera visual con los leds
- **buzzer.py** --> configuracion del buzzer
- **actuadores.py** --> funcion para activar la bomba y la valvula.