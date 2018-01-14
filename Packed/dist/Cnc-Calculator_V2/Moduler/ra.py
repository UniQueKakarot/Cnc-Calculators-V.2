from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.properties import ObjectProperty

from Moduler.customwidgets import MyLabel

Builder.load_string(
"""

<BoxLayout>:
    orientation: 'horizontal'
    
<Ra>:
    
    cols: 1
    padding: 10
    spacing: 10
    
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Feedrate: "
            
        TextInput:
            hint_text: "mm/o"
            multiline: False
            write_tab: False
            
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Nose Radius: "
        
        TextInput:
            hint_text: "mm"
            multiline: False
            write_tab: False
    
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Button:
            text: "Calculate!"
    
    BoxLayout:
        #size_hint_y: None
        #height: "200dp"
        Label:
            
    BoxLayout:
        size_hint_y: None
        height: "40dp"
        MyLabel:
            text: "Ra: "
            bcolor: [1, 1, 1, 0.15]
            
        MyLabel:
            text:
            bcolor: [1, 1, 1, 0.15]
            
"""
)


class Ra(GridLayout):        
    pass