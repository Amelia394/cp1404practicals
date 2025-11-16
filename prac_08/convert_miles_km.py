"""
CP1404 Practical 8
converting miles to km
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window

__author__ = 'Amelia Wilson'
MILES_CONVERSION = 1.60934

class ConvertMilesKmApp(App):
    def build(self):
        """Build the Kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file("convert_miles_km.kv")
        return self.root

    def handle_calculation(self):
        """Convert miles to km."""
        miles_value = self.get_valid_miles()
        km_value = miles_value * MILES_CONVERSION
        self.root.ids.km_label.text = str(km_value)

    def handle_increment(self, change):
        """Function for un and down increment button."""
        value = self.get_valid_miles() + change
        self.root.ids.input_number.text = str(value)
        self.handle_calculation()

    def get_valid_miles(self):
        """Makes sure the input is a valid mile."""
        try:
            value = float(self.root.ids.input_number.text)
            return value
        except ValueError:
            return 0


ConvertMilesKmApp().run()