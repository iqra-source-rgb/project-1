from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class SquareApp(App):
    def build(self):
        # Main layout for the app
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # Input field for the user to enter a number
        self.input_text = TextInput(
            hint_text="Enter a number",
            input_filter='float',  # Only allow numbers and a single decimal
            multiline=False
        )
        layout.add_widget(self.input_text)

        # Button that triggers the calculation
        calculate_button = Button(text="Calculate Square")
        calculate_button.bind(on_press=self.calculate_square)
        layout.add_widget(calculate_button)

        # Label to display the result
        self.result_label = Label(text="Result will appear here")
        layout.add_widget(self.result_label)

        return layout

    def calculate_square(self, instance):
        # Get the input, calculate square, and display it
        try:
            number = float(self.input_text.text)
            result = number ** 2
            self.result_label.text = f"The square of {number} is {result}"
        except ValueError:
            self.result_label.text = "Please enter a valid number!"


# Run the app
if __name__ == "__main__":
    SquareApp().run()
