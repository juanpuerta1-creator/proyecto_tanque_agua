import flet as ft
from colores import Colores

def crear_encabezado():
    encabezado = ft.Row(
        controls = [
            ft.Icon(ft.Icons.WATER_DROP, color = Colores["Turquesa"], size = 30),
            ft.Text("Acuarella", size = 20, weight = ft.FontWeight.BOLD, color = Colores["Texto"])
        ],
        spacing = 10,
        alignment = ft.MainAxisAlignment.CENTER
    )
    return encabezado