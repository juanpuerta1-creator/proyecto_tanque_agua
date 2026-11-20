
import flet as ft

from colores import Colores
from barra_lateral import crear_items, cuenta_usuario
from encabezado import crear_encabezado, encabezado_principal
from tarjetas import crear_tarjeta
from grafica import crear_grafica
from alertas import comprobar_alertas, recomendacion_limpieza
from tanque import crear_tanque
from panel_temperatura import crear_panel_temperatura


nivel = 56
ciclos = 100
ciclos_maximos = 100
temperatura_agua = 24.0


def main(page: ft.Page):

    page.title = "Acuarella - Monitor de tanque de agua"
    page.bgcolor = Colores["Fondo"]
    page.window.width = 1200
    page.window.height = 800
    page.window.min_width = 600
    page.window.min_height = 400

    # ENCABEZADOS
    encabezado = crear_encabezado()
    encabezado_2 = encabezado_principal()

    # BARRA LATERAL
    barra_lateral = ft.Container(
        width=220,
        bgcolor=Colores["Barra_lateral"],
        padding=10,
        border_radius=15,

        content=ft.Column(
            controls=[
                encabezado,

                ft.Text(
                    "MENU PRINCIPAL",
                    color=Colores["Texto_Secundario"],
                    size=12,
                    weight=ft.FontWeight.BOLD
                ),

                crear_items(ft.Icons.DASHBOARD, "Vista general", True),
                crear_items(ft.Icons.STORAGE, "Tanques"),
                crear_items(ft.Icons.SHOW_CHART, "Historial"),
                crear_items(ft.Icons.NOTIFICATIONS_NONE, "Alertas"),

                ft.Container(expand=True),

                cuenta_usuario(
                    "Juan Puerta",
                    "Administrador Principal",
                    "JP"
                )
            ]
        )
    )

    # TARJETAS DE INFORMACION
    espacio_tarjetas = ft.Row(
        controls=[
            crear_tarjeta(
                "Nivel del agua",
                "56%",
                ft.Icons.WATER_DROP,
                Colores["Turquesa"]
            ),

            crear_tarjeta(
                "Volumen del tanque",
                "14.000 L",
                ft.Icons.WATER,
                Colores["Turquesa"]
            ),

            crear_tarjeta(
                "Estado de la bomba",
                "ACTIVA",
                ft.Icons.WIFI,
                Colores["Turquesa"]
            ),
        ],
        spacing=10
    )

    # TANQUE Y GRAFICA
    espacio_tanque_grafica = ft.Row(
        controls=[
            crear_tanque(nivel),

            ft.Container(
                content=crear_grafica(),
                expand=True
            )
        ],
        spacing=15,
        vertical_alignment=ft.CrossAxisAlignment.START
    )

    # PANEL DE TEMPERATURA
    panel_temperatura = crear_panel_temperatura(
        temperatura_agua
    )

    # AREA PRINCIPAL
    area_principal = ft.Container(
        expand=True,
        padding=10,

        content=ft.Column(
            controls=[
                encabezado_2,

                espacio_tarjetas,

                espacio_tanque_grafica,

                panel_temperatura,

                comprobar_alertas(nivel),

                recomendacion_limpieza(ciclos, ciclos_maximos)
                if ciclos >= ciclos_maximos
                else ft.Container()
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        )
    )

    # ESTRUCTURA PRINCIPAL
    estructura_principal = ft.Row(
        expand=True,
        spacing=5,

        controls=[
            barra_lateral,
            area_principal
        ]
    )

    page.add(estructura_principal)


ft.run(main)