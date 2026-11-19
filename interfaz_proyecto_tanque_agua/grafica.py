import flet as ft
import flet_charts as fch
from colores import Colores

datos = [
    {"hora": "8:40", "nivel": 43.0},
    {"hora": "9:00", "nivel": 67.0},
    {"hora": "2:00", "nivel": 76.0},
    {"hora": "12:30", "nivel": 90.0},
    {"hora": "4:45", "nivel": 56.0},
]

Nivel_Min = 20
Nivel_Max = 90

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

    nivel_minimo = fch.LineChartData(
        points = [
            fch.LineChartDataPoint(0, Nivel_Min),
            fch.LineChartDataPoint(len(datos) - 1, Nivel_Min)
        ],
        color = Colores["Nivel_Min"],
        curved = False,
        dash_pattern = [5, 5]
    )

    nivel_maximo = fch.LineChartData(
        points = [
            fch.LineChartDataPoint(0, Nivel_Max),
            fch.LineChartDataPoint(len(datos) - 1, Nivel_Max)
        ],
        color = Colores["Nivel_Max"],
        curved = False,
        dash_pattern = [5, 5]
    )

    eje_vertical = fch.ChartAxis(
        labels = [
            fch.ChartAxisLabel(
                value = 0,
                label = ft.Text("0%", color=Colores["Texto_Secundario"])
            ),
            fch.ChartAxisLabel(
                value = 20,
                label = ft.Text("20%", color=Colores["Texto_Secundario"])
            ),
            fch.ChartAxisLabel(
                value = 40,
                label = ft.Text("40%", color=Colores["Texto_Secundario"])
            ),
            fch.ChartAxisLabel(
                value = 60,
                label = ft.Text("60%", color=Colores["Texto_Secundario"])
            ),
            fch.ChartAxisLabel(
                value = 80,
                label = ft.Text("80%", color=Colores["Texto_Secundario"])
            ),
            fch.ChartAxisLabel(
                value = 100,
                label = ft.Text("100%", color=Colores["Texto_Secundario"])
            )
        ],
        label_size = 50,
        label_spacing = 5
    )

    eje_horizontal = fch.ChartAxis(
        labels = [
            fch.ChartAxisLabel(
                value = i,
                label = ft.Text(
                    dato["hora"],
                    size = 10,
                    color = Colores["Texto_Secundario"]
                )
            )
            for i, dato in enumerate(datos)
        ]
    )

    grafica = fch.LineChart(
        data_series = [linea, nivel_minimo, nivel_maximo],
        min_x =  0,
        max_x = len(datos) - 1,
        min_y = 0,
        max_y = 100,
        left_axis = eje_vertical,
        bottom_axis = eje_horizontal,
        expand = True,
        horizontal_grid_lines = fch.ChartGridLines(
            interval = 10,
            color = Colores["Fondo"],
            width = 2
        ),

        tooltip = fch.LineChartTooltip(
            bgcolor = Colores["Fondo"],
            border_radius = 15,
            padding = 10,
            max_width = 120,
            fit_inside_vertically = True,
            fit_inside_horizontally = True
        ),
    )

    return ft.Container(
        height = 250,
        padding = 15,
        bgcolor = Colores["Barra_lateral"],
        border_radius = 15,
        content = grafica
    )
