import reflex as rx
import proyecto_link.constants as const
from proyecto_link.components.link_sponsor import link_sponsor
from proyecto_link.components.title import title
from proyecto_link.styles.styles import Size as Size

def sponsors() -> rx.Component: 
    return rx.vstack(
        title ("Colabora"),
        rx.hstack(
            link_sponsor(
                "/elgato.png",
                const.ELGATO_URL,
                "LogoTipoElGato"
            ),
            link_sponsor(
                "/mvp.png",
                const.MVP_URL,
                "LogoTipoSponsor"
            ),
            link_sponsor(
                "/githubstar.png",
                const.GITHUB_STAR_URL,
                "Logotipo de Github Star"
            ),
            spacing = Size.BIG.value,
            columns=[1,3]
        ),
        width = "100%",
        align_items = "start",
        spacing = Size.MEDIUM.value,
    )