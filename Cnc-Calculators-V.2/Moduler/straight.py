from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

from Moduler.customwidgets import MyLabel

Builder.load_string(
    """
    
<BoxLayout>:
    orientation: 'horizontal'
    
<Label>:
    font_size: 20

<TextInput>:
    font_size: 20

<Straight>:
    cols: 1
    padding: 10
    spacing: 10
    
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Toolpath Lenght: "
        TextInput:
            hint_text: "mm"
            multiline: False
            write_tab: False
            
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Step/Pitch: "
        TextInput:
            hint_text: "Z Step"
            multiline: False
            write_tab: False
            
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Button:
            text: "Calculate"
            
    Label:
            
    BoxLayout:
        size_hint_y: None
        height: "40dp"
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

class Straight(GridLayout):
    angle = StringProperty()
    pass
    