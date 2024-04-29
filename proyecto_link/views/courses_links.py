import reflex as rx
import proyecto_link.constants as const
from proyecto_link.components.link_button import link_button
from proyecto_link.components.title import title
from proyecto_link.components.newsletter import newsletter
from proyecto_link.styles.styles import Color, Spacing


def courses_links() -> rx.Component:
    return rx.vstack(
        title("Cursos gratis"),
        link_button(
            "Retos de programación",
            "Ruta de estudio semanal para practicar lógica",
            "/icons/challenges.png",
            const.CODE_CHALLENGES_URL,
            highlight_color=Color.SECONDARY.value
        ),
        link_button(
            "Python desde cero",
            "Curso de +37h: Fundamentos, frontend, backend, testing...",
            "/icons/python.svg",
            const.PYTHON_COURSE_URL
        ),
        link_button(
            "Git y GitHub",
            "Curso de 5h para aprender Git y GitHub desde cero",
            "/icons/git.svg",
            const.GIT_COURSE_URL
        ),
        link_button(
            "SQL y Bases de Datos",
            "Curso de 7h desde cero para aprender los fundamentos de SQL",
            "/icons/sql.svg",
            const.SQL_COURSE_URL
        ),
        link_button(
            "Un día, un lenguaje",
            "Primeros pasos en los 11 lenguajes de programación más usados",
            "/icons/code.svg",
            const.LANGUAGES_COURSE_URL
        ),

        title("Mucho más en"),
        link_button(
            "Twitch",
            "Transmisiones sobre programación de lunes a viernes",
            "/icons/twitch.svg",
            const.TWITCH_URL
        ),
        link_button(
            "YouTube",
            "Tutoriales sobre desarrollo de software semanales",
            "/icons/youtube.svg",
            const.YOUTUBE_URL
        ),
        link_button(
            "YouTube [canal secundario]",
            "Emisiones en directo destacadas",
            "/icons/youtube.svg",
            const.YOUTUBE_SECONDARY_URL
        ),
        newsletter(),
        width="100%",
        spacing=Spacing.DEFAULT.value,
    )