import flet as ft

def main(page: ft.Page):
    page.add(
        ft.Text('Vito'),
        ft.ElevatedButton('Clique Aqui')
    )

ft.run(main)