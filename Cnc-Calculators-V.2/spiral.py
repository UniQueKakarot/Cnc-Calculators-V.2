from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

import MyLabel

Builder.load_string(
    """
<BoxLayout>:
    orientation: 'horizontal'

<Label>:
    font_size: 20
    size_hint: 0.5, 1
    
<TextInput>:
    font_size: 20
    size_hint: 0.5, 1
    multiline: False
    write_tab: False
    
<Spiral>:
    
    GridLayout:
        cols: 1
        padding: 10
        spacing: 15
        
        BoxLayout:
            Label:
                text: "Mill Diameter:"
                
            TextInput:
                focus: True
            
        BoxLayout:
            Label:
                text: "Hole Diameter:"
                
            TextInput:
            
        BoxLayout:
            Label:
                text: "Step/Pitch:"
                
            TextInput:
            
        Button:
            text: "Calc"
            size_hint: 0.5, 1
            
        BoxLayout:
            MyLabel:
                text: "Angle:"
                font_size: 20
                bcolor: [1, 1, 1, 0.15]
                
            MyLabel:
                text: root.angle
                font_size: 20
                bcolor: [1, 1, 1, 0.15]
                
    """
)

class Spiral(FloatLayout):
    
    angle = StringProperty()
    
    def __init__(self, **kwargs):
        super(Spiral, self).__init__(**kwargs)
        
    def dummy(self):
        print('Hello World!')