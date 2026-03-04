import flet as ft

def main(page: ft.Page):
    page.title = "Gestión de Eventos"
    page.padding = 25

    titulo = ft.Text(
        value="Formulario de Registro de Evento",
        size=30,
        weight=ft.FontWeight.BOLD,
        color=ft.Colors.GREEN_900
    )

    nombre_evento = ft.TextField(
        label="Nombre del evento",
        hint_text="Ingrese el nombre del evento",
        border=ft.InputBorder.OUTLINE,
        filled=True,
        bgcolor=ft.Colors.GREEN_100
    )

    tipo_evento = ft.Dropdown(
        label="Tipo de evento",
        options=[
            ft.dropdown.Option("Conferencia"),
            ft.dropdown.Option("Taller"),
            ft.dropdown.Option("Reunión"),
        ],
        value="Conferencia"
    )

    modalidad = ft.RadioGroup(
        content=ft.Row(
            controls=[
                ft.Radio(value="Presencial", label="Presencial"),
                ft.Radio(value="Virtual", label="Virtual"),
            ],
            spacing=20
        ),
        value="Presencial"
    )

    inscripcion = ft.Checkbox(
        label="¿Requiere inscripción previa?",
        value=False
    )

    duracion = ft.Slider(
        min=1,
        max=8,
        divisions=7,
        label="{value} horas",
        value=1
    )

    resumen_texto = ft.Text(
        value="",
        size=16,
        weight=ft.FontWeight.W_500,
        color=ft.Colors.GREEN_800
    )

    def mostrar_resumen(e):
        if not nombre_evento.value:
            resumen_texto.value = " Error: El nombre del evento no puede estar vacío."
            resumen_texto.color = ft.Colors.RED
        else:
            resumen_texto.color = ft.Colors.GREEN_800
            resumen_texto.value = (
                f"Nombre del evento: {nombre_evento.value}\n"
                f"Tipo de evento: {tipo_evento.value}\n"
                f"Modalidad: {modalidad.value}\n"
                f"Requiere inscripción previa: {'Sí' if inscripcion.value else 'No'}\n"
                f"Duración estimada: {int(duracion.value)} horas"
            )
        page.update()

    boton_resumen = ft.ElevatedButton(
        "Mostrar resumen",
        on_click=mostrar_resumen,
        bgcolor=ft.Colors.BLUE,
        color=ft.Colors.WHITE
    )

    page.add(
        ft.Column(
            controls=[
                titulo,
                nombre_evento,
                tipo_evento,
                modalidad,
                inscripcion,
                duracion,
                ft.Row([boton_resumen], alignment=ft.MainAxisAlignment.CENTER),
                ft.Divider(),
                resumen_texto,
            ],
            spacing=20,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

if __name__ == "__main__":
    ft.app(target=main)