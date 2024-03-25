# from kivy.app import App
from kivy.uix.gridlayout import GridLayout
# from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.config import Config
# from kivymd.theming import ThemeManager
from kivymd.app import MDApp


Config.set('kivy', 'kyeboard_mode', 'systemanddock')
Window.size = (360, 720)


class Container(GridLayout):

    def convert(self):
        try:
            number = int(self.text_input.text)
        except Exception:
            number = 0

        self.label_hours.text = str(number * 24)
        self.label_minutes.text = str(number * 24 * 60)
        self.label_seconds.text = str(number * 24 * 360)
        self.label_milliseconds.text = str(number * 24 * 360 * 60)


class DWApp(MDApp):

    def __init__(self, **kwargs):
        self.title = "DW App"
        super().__init__(**kwargs)

    def build(self):
        return Container()


if __name__ == "__main__":
    DWApp().run()