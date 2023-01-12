import flet as ft
from utils import LANGUAGES

class Translator(ft.UserControl):
    def build(self):
        self.lan_options = [ft.dropdown.Option(key=lan['code'], text=lan['label']) for lan in LANGUAGES]
        dd_source_lan = ft.Dropdown(options=self.lan_options, value="auto", width=180)
        dd_target_lan = ft.Dropdown(options=self.lan_options[1:], value="en", width=180)

        tf_input = ft.Container(
            width=500,
            height=400,
            content=ft.TextField(border=ft.InputBorder.NONE, text_size=20, multiline=True, autofocus=True, hint_text="Enter Text"),
            border_radius=ft.border_radius.all(5),
            border=ft.border.all(1, color=ft.colors.BLACK),
            padding=20,
            expand=True
        )
        tf_output = ft.Container(
            width=500,
            height=400,
            content=ft.TextField(border=ft.InputBorder.NONE, text_size=20, multiline=True, hint_text="Translation"),
            border_radius=ft.border_radius.all(5),
            border=ft.border.all(1, color=ft.colors.BLACK),
            bgcolor=ft.colors.BLUE_GREY_50,
            padding=20,
            expand=True,
            disabled=True
        )

        lan_choice = ft.Container(
            content=ft.Row(
                [
                    dd_source_lan,
                    ft.IconButton(
                        icon=ft.icons.SWAP_HORIZ_SHARP
                    ),
                    dd_target_lan
                ]
            ),
            expand=True
        )

        view = ft.Column(
            [
                ft.Row(
                    [
                        lan_choice,
                        ft.IconButton(
                            icon=ft.icons.LIGHT_MODE_SHARP,
                            tooltip="Toggle Dark/Light Theme",
                            on_click=self.toggle_theme_clicked,
                            data="light"
                        )
                    ]
                ),
                ft.Row(
                    [
                        tf_input,
                        ft.VerticalDivider(),
                        tf_output
                    ]
                ),
                ft.Row(
                    [
                        ft.IconButton(
                            icon=ft.icons.STAR_PURPLE500_SHARP,
                            tooltip="View Project on GitHub",
                            on_click=lambda _: self.page.launch_url("https://github.com/codingZXY/FletApps/tree/main/Translator")
                        ),
                        ft.Text("LuckOverflow", color=ft.colors.BLUE_GREY, italic=True),
                    ]
                )
            ]
        )

        return view

    def toggle_theme_clicked(self, e):
        current = e.control.data

        if current == ft.ThemeMode.LIGHT.value:
            e.control.data = ft.ThemeMode.DARK.value
            e.control.icon = ft.icons.DARK_MODE_SHARP
            self.update()

            self.page.theme_mode = ft.ThemeMode.DARK
            self.page.update()

        else:
            e.control.data = ft.ThemeMode.LIGHT.value
            e.control.icon = ft.icons.LIGHT_MODE_SHARP
            self.update()

            self.page.theme_mode = ft.ThemeMode.LIGHT
            self.page.update()




def main(page:ft.Page):
    page.title = "Translator"
    page.window_height = 620
    page.window_width = 1280
    page.window_resizable = True
    page.window_maximizable = False
    page.window_title_bar_hidden = True
    page.window_title_bar_buttons_hidden = True

    page.window_opacity = 1
    page.theme_mode = ft.ThemeMode.LIGHT

    def minimize(e):
        page.window_minimized = True
        page.update()

    header = ft.Row(
        [
            ft.WindowDragArea(
                ft.Container(ft.Text(value="Translator App", style=ft.TextThemeStyle.HEADLINE_MEDIUM),
                             bgcolor=ft.colors.TRANSPARENT, padding=10, margin=0), expand=True
            ),
            ft.IconButton(ft.icons.MINIMIZE, on_click=minimize),
            ft.IconButton(ft.icons.CLOSE, on_click=lambda _: page.window_close()),
        ],
        visible=not page.web,
    )
    translator = Translator()
    page.add(header)
    page.add(translator)




ft.app(target=main)