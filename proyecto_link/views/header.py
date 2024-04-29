import reflex as rx
import datetime
import proyecto_link.constants as const
from proyecto_link.styles.styles import Size, Spacing
from proyecto_link.styles.colors import Color, TextColor
from proyecto_link.components.link_icon import link_icon
from proyecto_link.components.info_text import info_text
from proyecto_link.components.link_button import link_button


def header(details=True) -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.box(
                    rx.link(
                        rx.image(
                            src="/icons/twitch.svg",
                            height=Size.DEFAULT.value,
                            width=Size.DEFAULT.value
                        ),
                        href=const.TWITCH_URL,
                        is_external=True,
                        class_name="blink",
                        border_radius="50%",
                        padding=Size.SMALL.value,
                        bg=Color.PURPLE.value,
                        position="absolute",
                        bottom="0",
                        right="0",
                ),
                rx.avatar(
                    name="Bastian Ibáñez",
                    size=Spacing.MEDIUM_BIG.value,
                    src="/avatar.jpg.jpeg",
                    radius="full",
                    color=TextColor.BODY.value,
                    bg=Color.CONTENT.value,
                    padding="2px",
                    border=f"4px solid {Color.PRIMARY.value}"
                ),
                position="relative"
            ),
            rx.vstack(
                rx.heading(
                    "Bastian Ibáñez",
                    size=Spacing.BIG.value
                ),
                rx.text(
                    "bibanez",
                    margin_top=Size.ZERO.value,
                    color=Color.PRIMARY.value
                ),
                rx.hstack(
                    link_icon(
                        "/icons/github.svg",
                        const.GITHUB_URL,
                        "GitHub"
                    ),
                    link_icon(
                        "/icons/x.svg",
                        const.TWITTER_X_URL,
                        "Twitter/X"
                    ),
                    link_icon(
                        "/icons/instagram.svg",
                        const.INSTAGRAM_URL,
                        "Instagram"
                    ),
                    link_icon(
                        "/icons/tiktok.svg",
                        const.TIKTOK_URL,
                        "TikTok"
                    ),
                    link_icon(
                        "/icons/spotify.svg",
                        const.SPOTIFY_URL,
                        "Spotify"
                    ),
                    link_icon(
                        "/icons/linkedin.svg",
                        const.LINKEDIN_URL,
                        "LinkedIn"
                    ),
                    spacing=Spacing.LARGE.value,
                    padding_top=Size.SMALL.value
                ),
                spacing=Spacing.ZERO.value,
                align_items="start"
            ),
            align="end",
            spacing=Spacing.DEFAULT.value
        ),
        rx.cond(
            details,
            rx.vstack(
                rx.flex(
                    info_text(
                        f"{experience()}+",
                        "años de experiencia"
                    ),
                    rx.spacer(),
                    info_text(
                        "100+", "Ejercicios"
                    ),
                    rx.spacer(),
                    info_text(
                        "Y", "más"
                    ),
                    width="100%"
                ),
                    link_button(
                        "En directo",
                        "directos de twitch",
                        "/icons/twitch.svg",
                        const.TWITCH_URL,
                        highlight_color=Color.PURPLE.value,
                        animated=True
                    ),
                    rx.box(
                            link_button(
                                "Próximo directo",
                                "asdasd",
                                "/icons/twitch.svg",
                                const.TWITCH_URL,
                                highlight_color=Color.PURPLE.value,
                                animated=True
                            ),
                        width="100%",
                    ),
                rx.text(
                    f"""
                    Profesional, Certificado en programación full stack java. 
                    Estudiante de la academia de Coding Dojo, con un especial interés en el area de bases de datos, 
                    de ciencias de datos y en el area de ciberseguridad. 
                    Mi experiencia en el campo son practicas, realizando proyectos de desarrollador en backend como en frontend utilizando disitntos Framework. 
                    ¡Bienvenid@!
                    """,
                    font_size=Size.DEFAULT.value,
                    color=TextColor.BODY.value
                ),
                width="100%",
                spacing=Spacing.BIG.value
            )
        ),
        width="100%",
        spacing=Spacing.BIG.value,
        align_items="start",
    )


def experience() -> int:
    return datetime.date.today().year - 2023