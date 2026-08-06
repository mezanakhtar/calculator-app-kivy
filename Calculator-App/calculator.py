from kivy.app import App
from kivy.lang import Builder

KV = '''
BoxLayout:
    orientation: 'vertical'
    padding: 10
    spacing: 5

    TextInput:
        id: display
        text: "0"
        font_size: "49sp"
        multiline: False
        readonly: True
        halign: "right"
        size_hint_y: 0.2

    GridLayout:
        cols: 4
        spacing: "5dp"
        padding: "10dp"

        Button:
            text: "7"
            on_release: app.on_button_press("7")
        Button:
            text: "8"
            on_release: app.on_button_press("8")
        Button:
            text: "9"
            on_release: app.on_button_press("9")
        Button:
            text: "÷"
            on_release: app.on_button_press("/")

        Button:
            text: "4"
            on_release: app.on_button_press("4")
        Button:
            text: "5"
            on_release: app.on_button_press("5")
        Button:
            text: "6"
            on_release: app.on_button_press("6")
        Button:
            text: "×"
            on_release: app.on_button_press("*")

        Button:
            text: "1"
            on_release: app.on_button_press("1")
        Button:
            text: "2"
            on_release: app.on_button_press("2")
        Button:
            text: "3"
            on_release: app.on_button_press("3")
        Button:
            text: "-"
            on_release: app.on_button_press("-")

        Button:
            text: "C"
            on_release: app.clear_display()
        Button:
            text: "0"
            on_release: app.on_button_press("0")
        Button:
            text: "="
            on_release: app.calculate_result()
        Button:
            text: "+"
            on_release: app.on_button_press("+")
'''

class CalculatorApp(App):

    def build(self):
        return Builder.load_string(KV)

    def on_button_press(self, value):
        display = self.root.ids.display

        if display.text == "0":
            if value in "+-×÷":
                return
            display.text = value
        else:
            display.text += value

    def calculate_result(self):
        display = self.root.ids.display

        try:
            result = eval(display.text)
            display.text = str(result)
        except Exception:
            display.text = "Error"

    def clear_display(self):
        self.root.ids.display.text = "0"

if __name__ == "__main__":
    CalculatorApp().run()