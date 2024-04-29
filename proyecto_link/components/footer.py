import reflex as rx
import datetime
import proyecto_link.constants as const
from proyecto_link.styles.styles import Size as Size
from proyecto_link.styles.styles import Size, Spacing
from proyecto_link.components.ant_components import Color
from proyecto_link.styles.colors import TextColor as TextColor
from proyecto_link.components.ant_components import float_button



def footer() -> rx.Component:
    return rx.vstack(
        rx.image(
            src="/keyboard-solid.svg",
            height= 170,
            width= 170,
            alt="Logo que modificar"
        ),
        rx.link(
            rx.box(
                f"© 2023-{datetime.date.today().year} ",
                rx.text(
                    "bibanez by Bastian Ibáñez",
                    as_="span",
                    color=Color.PRIMARY.value
                ),
                " v4.",
                padding_top=Size.DEFAULT.value
            ),
            href=const.MOUREDEV_URL,
            is_external=True,
            font_size=Size.MEDIUM.value
        ),
        rx.link(
            rx.hstack(
                rx.image(
                    src="/icons/github.svg",
                    height=Size.LARGE.value,
                    width=Size.LARGE.value,
                    alt="Logo GitHub"
                ),
                rx.text(
                    "BUILDING SOFTWARE WITH ♥ FROM GALICIA TO THE WORLD.",
                    font_size=Size.MEDIUM.value,
                    margin_top=Size.ZERO.value
                ),
            ),
            href=const.REPO_URL,
            is_external=True
        ),
        float_button(
            icon=rx.image(src="/icons/donate.svg"),
            href=const.COFFEE_URL
        ),
        align="center",
        margin_bottom=Size.BIG.value,
        padding_bottom=Size.VERY_BIG.value,
        padding_x=Size.BIG.value,
        spacing=Spacing.ZERO.value,
        color=TextColor.FOOTER.value
    )