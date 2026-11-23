import flet as ft
from colores import Colores
from barra_lateral import crear_items, cuenta_usuario
from encabezado import crear_encabezado, encabezado_principal
from tarjetas import crear_tarjeta
from grafica import crear_grafica
from alertas import comprobar_alertas, recomendacion_limpieza
from tanque import crear_tanque
from panel_temperatura import crear_panel_temperatura


# VARIABLES DEL SISTEMA
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

    # CONTENEDOR DONDE SE MOSTRARAN LAS DIFERENTES VISTAS
    contenido_principal = ft.Container(
        expand=True,
        padding=10
    )

    # VISTA GENERAL
    def vista_general():

        espacio_tarjetas = ft.Row(
            controls=[
                crear_tarjeta(
                    "Nivel del agua",
                    f"{nivel}%",
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

                crear_tarjeta(
                    "Temperatura",
                    f"{temperatura_agua} °C",
                    ft.Icons.THERMOSTAT,
                    Colores["Turquesa"]
                )
            ],
            spacing=10
        )

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

        return ft.Column(
            controls=[
                encabezado_2,
                espacio_tarjetas,
                espacio_tanque_grafica,
                crear_panel_temperatura(temperatura_agua),
                comprobar_alertas(nivel),

                recomendacion_limpieza(ciclos, ciclos_maximos)
                if ciclos >= ciclos_maximos
                else ft.Container()
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        )

    # VISTA DE TANQUES
    def vista_tanques():

        return ft.Column(
            controls=[
                ft.Text(
                    "Monitoreo de tanques",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    color=Colores["Texto"]
                ),

                ft.Text(
                    "Información detallada del tanque principal",
                    size=14,
                    color=Colores["Texto_Secundario"]
                ),

                ft.Row(
                    controls=[
                        crear_tanque(nivel),

                        ft.Container(
                            expand=True,
                            padding=20,
                            bgcolor=Colores["Barra_lateral"],
                            border_radius=15,

                            content=ft.Column(
                                controls=[
                                    ft.Text(
                                        "Información del tanque",
                                        size=18,
                                        weight=ft.FontWeight.BOLD,
                                        color=Colores["Texto"]
                                    ),

                                    ft.Text(
                                        "Tanque principal",
                                        size=14,
                                        color=Colores["Texto_Secundario"]
                                    ),

                                    ft.Divider(
                                        color=Colores["Texto_Secundario"]
                                    ),

                                    ft.Text(
                                        f"Nivel actual: {nivel}%",
                                        color=Colores["Texto"],
                                        size=15
                                    ),

                                    ft.Text(
                                        "Capacidad: 20.000 litros",
                                        color=Colores["Texto"],
                                        size=15
                                    ),

                                    ft.Text(
                                        f"Temperatura: {temperatura_agua} °C",
                                        color=Colores["Texto"],
                                        size=15
                                    ),

                                    ft.Text(
                                        "Altura máxima: 4 metros",
                                        color=Colores["Texto"],
                                        size=15
                                    )
                                ],
                                spacing=15
                            )
                        )
                    ],
                    vertical_alignment=ft.CrossAxisAlignment.START,
                    spacing=15
                ),

                crear_panel_temperatura(temperatura_agua)
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        )

    # VISTA DE HISTORIAL
    def vista_historial():

        return ft.Column(
            controls=[
                ft.Text(
                    "Historial de mediciones",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    color=Colores["Texto"]
                ),

                ft.Text(
                    "Evolución del nivel del agua en el tanque",
                    size=14,
                    color=Colores["Texto_Secundario"]
                ),

                crear_grafica()
            ],
            spacing=20,
            scroll=ft.ScrollMode.AUTO
        )

    # VISTA DE ALERTAS
    def vista_alertas():

        return ft.Column(
            controls=[
                ft.Text(
                    "Alertas del sistema",
                    size=25,
                    weight=ft.FontWeight.BOLD,
                    color=Colores["Texto"]
                ),

                ft.Text(
                    "Estado y notificaciones del tanque",
                    size=14,
                    color=Colores["Texto_Secundario"]
                ),

                comprobar_alertas(nivel),

                recomendacion_limpieza(ciclos, ciclos_maximos)
                if ciclos >= ciclos_maximos
                else ft.Container()
            ],
            spacing=15,
            scroll=ft.ScrollMode.AUTO
        )

    # FUNCION PARA CAMBIAR DE PANTALLA
    def mostrar_vista(nombre):

        if nombre == "Vista general":
            contenido_principal.content = vista_general()

        elif nombre == "Tanques":
            contenido_principal.content = vista_tanques()

        elif nombre == "Historial":
            contenido_principal.content = vista_historial()

        elif nombre == "Alertas":
            contenido_principal.content = vista_alertas()

        page.update()

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

                crear_items(
                    ft.Icons.DASHBOARD,
                    "Vista general",
                    True,
                    on_click=lambda e: mostrar_vista("Vista general")
                ),

                crear_items(
                    ft.Icons.STORAGE,
                    "Tanques",
                    on_click=lambda e: mostrar_vista("Tanques")
                ),

                crear_items(
                    ft.Icons.SHOW_CHART,
                    "Historial",
                    on_click=lambda e: mostrar_vista("Historial")
                ),

                crear_items(
                    ft.Icons.NOTIFICATIONS_NONE,
                    "Alertas",
                    on_click=lambda e: mostrar_vista("Alertas")
                ),

                ft.Container(expand=True),

                cuenta_usuario(
                    "Juan Puerta",
                    "Administrador Principal",
                    "JP"
                )
            ]
        )
    )

    # MOSTRAR VISTA INICIAL
    contenido_principal.content = vista_general()

    # ESTRUCTURA PRINCIPAL
    estructura_principal = ft.Row(
        expand=True,
        spacing=5,

        controls=[
            barra_lateral,
            contenido_principal
        ]
    )

    page.add(estructura_principal)


ft.run(main)