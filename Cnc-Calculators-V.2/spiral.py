from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder

Builder.load_string(
    """
<Spiral>:

    BoxLayout:
        Button:
            text: "Hello World!"
            on_press: root.dummy()
    """
)

class Spiral(FloatLayout):
    
    def __init__(self, **kwargs):
        super(Spiral, self).__init__(**kwargs)
        
    def dummy(self):
        print('Hello World!')