import reflex as rx
import proyecto_link.styles.styles as styles
from proyecto_link.styles.styles import Size
from proyecto_link.styles.colors import Color
from proyecto_link.routes import Route
from proyecto_link.components.ant_components import float_button

def navbar() -> rx.Component:
    return rx.hstack(
        rx.link(
            rx.box(
                rx.text("B", as_="span", color=Color.PRIMARY.value),
                rx.text("ibanez", as_="span", color=Color.SECONDARY.value),
                style=styles.navbar_title_style
            ),
            href=Route.INDEX.value
        ),
        position="sticky",
        bg=Color.CONTENT.value,
        padding_x=Size.BIG.value,
        padding_y=Size.DEFAULT.value,
        z_index="999",
        top="0"
    )