import flet as ft
from flet import (
    UserControl,
    Text,
    Container,
    Column,
    Row,
    TextField,
    ElevatedButton
)
from itertools import permutations, product


FORMAT_STRINGS = ("(({0}{4}{1}){5}{2}){6}{3}",
                  "({0}{4}{1}){6}({2}{5}{3})",
                  "({0}{5}({1}{4}{2})){6}{3}",
                  "{0}{6}(({1}{4}{2}){5}{3})",
                  "{0}{6}({1}{5}({2}{4}{3}))")
EPS = 1e-6


def equal_to_24(a, b, c, d):
    for numbers, operators, format_string in product(
        permutations((a, b, c, d)),
        product("+-*/", repeat=3),
        FORMAT_STRINGS
    ):
        string = format_string.format(*numbers, *operators)
        try:
            if abs(eval(string) - 24) <= EPS: return string
        except: pass
    return "It's not possible!"


class Calc24(UserControl):
    def build(self):
        self.result = Text(value='')
        self.num1 = TextField(text_align=ft.TextAlign.CENTER, expand=True)
        self.num2 = TextField(text_align=ft.TextAlign.CENTER, expand=True)
        self.num3 = TextField(text_align=ft.TextAlign.CENTER, expand=True)
        self.num4 = TextField(text_align=ft.TextAlign.CENTER, expand=True)

        view = Container(
            width=350,
            content=Column(
                controls=[
                    ft.Row([ft.Text(value="24 Solver", style=ft.TextThemeStyle.HEADLINE_MEDIUM)], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text(value="Enter your 4 numbers below, then click 'Solve' to see the solution that equals 24.")]),
                    Row(
                        controls=[
                            self.num1,
                            self.num2,
                            self.num3,
                            self.num4,
                            ElevatedButton(text="Solve", on_click=self.solve_clicked)
                        ]
                    ),
                    Row(
                        alignment=ft.MainAxisAlignment.CENTER,
                        controls=[self.result]
                    )
                ]
            )
        )

        return view

    def check_num(self):
        return self.num1.value.isdigit() and self.num2.value.isdigit() \
               and self.num3.value.isdigit() and self.num4.value.isdigit()

    def solve_clicked(self, e):
        if not self.check_num():
            self.page.dialog = ft.AlertDialog(
                content=ft.Text("Please enter 4 numbers between 1 to 10.")
            )

            self.page.dialog.open = True
            self.page.update()

            return

        result = equal_to_24(self.num1.value, self.num2.value, self.num3.value, self.num4.value)
        self.result.value = result
        self.update()






def main(page: ft.Page):
    page.title = "24 Solver"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.update()

    calc24 = Calc24()

    page.add(calc24)



ft.app(target=main)