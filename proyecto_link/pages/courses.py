import reflex as rx
import proyecto_link.utils as utils
import proyecto_link.styles.styles as styles
from proyecto_link.routes import Route
from proyecto_link.components.navbar import navbar
from proyecto_link.components.footer import footer
from proyecto_link.views.header import header
from proyecto_link.views.courses_links import courses_links
from proyecto_link.views.sponsors import sponsors
from proyecto_link.styles.styles import Size


@rx.page(
    route=Route.COURSES.value,
    title=utils.courses_title,
    description=utils.courses_description,
    image=utils.preview,
    meta=utils.courses_meta
)
def courses() -> rx.Component:
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(False),
                courses_links(),
                sponsors(),
                max_width=styles.MAX_WIDTH,
                width="100%",
                margin_y=Size.BIG.value,
                padding=Size.BIG.value
            )
        ),
        footer()
    )