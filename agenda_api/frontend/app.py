import reflex as rx

# Estado de la app
class State(rx.State):
    usuarios: str = ""

    def fetch_usuarios(self):
        yield rx.get(
            "http://127.0.0.1:8000/usuarios/",
            callback=lambda data: setattr(self, "usuarios", str(data))
        )

# Página principal
def index():
    return rx.box(
        rx.heading("Listado de Usuarios"),
        rx.text(State.usuarios),
        rx.button("Actualizar Usuarios", on_click=State.fetch_usuarios),
        padding="2em"
    )

# Configuración de la app Reflex
app = rx.App()
app.add_page(index)



