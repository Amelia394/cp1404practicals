from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.names = ["Jim", "John", "Jason", "Jacob"]


DynamicLabelsApp().run()