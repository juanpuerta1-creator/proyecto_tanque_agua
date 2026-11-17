import flet as ft
import flet_charts as fch
from colores import Colores

datos = [
    {"hora": "8:40", "nivel": 43.0},
    {"hora": "9:00", "nivel": 67.0},
    {"hora": "12:30", "nivel": 90.0},
    {"hora": "4:45", "nivel": 90.0},
]

def crear_grafica():
    puntos = [
        fch.LineChartDataPoint(i, dato["nivel"])
        for i, dato in enumerate(datos)
    ]

    linea = fch.LineChartData(
        points = puntos,
        color = Colores["Turquesa"],
        stroke_width = 3,
        curved = True,
        point = True
    )

    grafica = fch.LineChart(
        data_series = [linea],
        min_x =  0,
        max_x = len(datos) - 1,
        min_y = 0,
        max_y = 100,
        expand = True
    )

    return ft.Container(
        height = 250,
        padding = 15,
        bgcolor = Colores["Barra_lateral"],
        border_radius = 15,
        content = grafica
    )
