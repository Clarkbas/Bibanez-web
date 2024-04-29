import reflex as rx
import proyecto_link.utils as utils
import proyecto_link.styles.styles as styles
from proyecto_link.components.navbar import navbar
from proyecto_link.components.footer import footer
from proyecto_link.views.header import header
from proyecto_link.views.index_links import index_links
from proyecto_link.views.sponsors import sponsors
from proyecto_link.styles.styles import Size


@rx.page(
    title=utils.index_title,
    description=utils.index_description,
    image=utils.preview,
    meta=utils.index_meta
)
def index() -> rx.Component: 
    return rx.box(
        utils.lang(),
        navbar(),
        rx.center(
            rx.vstack(
                header(),
                index_links(),
                sponsors(),
                max_width= styles.MAX_WIDTH,
                width="100%",
                margin_y= Size.BIG.value,
                padding=Size.BIG.value,
            ),
        ),
        footer(),
    )

