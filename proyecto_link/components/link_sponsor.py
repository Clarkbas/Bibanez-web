import reflex as rx
import proyecto_link.styles.styles as styles
from proyecto_link.styles.styles import Size as Size

def link_sponsor(imagen: str, url: str, alt: str) -> rx.Component:
    return rx.link(
        rx.image(
            src=imagen,
            height="3.5em",
            aspect_ratio="5 / 2",
            alt=alt
        ),
        href=url,
        is_external=True
    )