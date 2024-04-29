import reflex as rx
import proyecto_link.constants as constants
import proyecto_link.styles.styles as styles
from proyecto_link.styles.styles import Size as Size
from proyecto_link.pages.index import index
from proyecto_link.pages.courses import courses
#from proyecto_link.components.title import title

class State(rx.State):
    """ define your app state here """

app = rx.App(
    stylesheets= styles.STYLESHEETS,
    style=styles.BASE_STYLE,
    head_components=[
        rx.script(src=f"https://www.googletagmanager.com/ns.html?id={constants.G_TAG}"),
    ]
)



