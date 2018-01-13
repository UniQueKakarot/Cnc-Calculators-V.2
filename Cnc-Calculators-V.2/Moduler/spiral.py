from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

from Moduler.customwidgets import MyLabel
from Moduler import straight

Builder.load_string(
    """
<BoxLayout>:
    orientation: 'horizontal'

<Label>:
    font_size: 20
    
<TextInput>:
    font_size: 20
    multiline: False
    write_tab: False
    
<Spiral>:

    TabbedPanel:
        do_default_tab: False
        tab_pos: 'top_right'
        tab_height: 25
        
        TabbedPanelItem:
            text: 'Spiral'
            font_size: 15

            GridLayout:
                cols: 1
                padding: 10
                spacing: 10
        
                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: "Mill Diameter:"
                        
                    TextInput:
                        focus: True
                        hint_text: "mm"
                    
                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: "Hole Diameter:"
                        
                    TextInput:
                        hint_text: "ø"
                    
                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: "Step/Pitch:"
                        
                    TextInput:
                        hint_text: "Z step"
                
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
                            
        TabbedPanelItem:
            text: 'Straigth'
            font_size: 15
            Straight:
                
    """
)

class Spiral(FloatLayout):
    
    angle = StringProperty()
    
    def __init__(self, **kwargs):
        super(Spiral, self).__init__(**kwargs)
        
    def dummy(self):
        print('Hello World!')