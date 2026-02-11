import flet as ft

def main(page: ft.Page):
    page.title = 'Meu programa em flet'
    page.bgcolor = '#e010c8'
    page.vertical_alignment = ft.MainAxistAlignment.CENTER
    page.vertical_alignment = ft.CrossAxistAlignment.CENTER
    page.add(
        ft.Text('Vito'),
        ft.ElevatedButton('Clique Aqui')
    )

ft.run(main)