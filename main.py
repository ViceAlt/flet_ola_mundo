import flet as ft

def main(page: ft.Page):
    page.title = 'Meu programa em flet'
    page.bgcolor = '#e010c8'
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment= ft.CrossAxisAlignment.CENTER
    page.add(
        ft.Text('Vito'),
        ft.ElevatedButton('Clique Aqui')
    )

ft.run(main)