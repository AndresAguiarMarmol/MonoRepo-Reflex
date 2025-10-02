import reflex as rx

config = rx.Config(
    app_name="agenda_medica",
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
    ]
)