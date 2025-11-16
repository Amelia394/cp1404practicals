"""
Dynamically create labels based on content of dictionary
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """Create dynamic labels with names."""
    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Jimmy", "John", "Jason", "Jacob"]

    def build(self):
        """Show labels with names"""
        self.root = Builder.load_file("dynamic_labels.kv")
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.main.add_widget(name_label)
        return self.root

DynamicLabelsApp().run()