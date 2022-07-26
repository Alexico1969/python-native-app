"""
Fahrenheit to Celcius converter
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, LEFT, RIGHT, CENTER, BOTTOM, TOP


class FreedomUnits(toga.App):

    def startup(self):
        f_box = toga.Box(style=Pack(direction=ROW, padding=5))

        self.f_input = toga.TextInput(style=Pack(flex=1, padding_left=160))
        f_label = toga.Label('Fahrenheit', style=Pack(text_align=LEFT, width=100, padding_left=10))

        f_box.add(self.f_input)
        f_box.add(f_label)

        c_box = toga.Box(style=Pack(direction=ROW, padding=5))

        join_label = toga.Label(
            'is equivalent to',
            style=Pack(text_align=RIGHT, width=150, padding_right=10)
        )
        self.c_input = toga.TextInput(
            readonly=True,
            style=Pack(flex=1)
        )
        c_label = toga.Label(
            'Celcius', 
            style=Pack(text_align=LEFT, width=100, padding_left=10),
        )

        c_box.add(join_label)
        c_box.add(self.c_input)
        c_box.add(c_label)

        button = toga.Button(
            'Calculate',
            on_press=self.calculate,
            style=Pack(padding=15, flex=1),
        )



        main_box = toga.Box(style=Pack(direction=COLUMN, padding_top=10))
        main_box.add(f_box)
        main_box.add(c_box)
        main_box.add(button)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def calculate(self, widget, **kwargs):
        try:
            self.c_input_value = (float(self.f_input.value) - 32) * 5 / 9
        except:
            self.c_input_value = 'Invalid input'
        
def main():
    return FreedomUnits()
