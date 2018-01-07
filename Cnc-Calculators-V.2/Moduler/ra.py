from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_string(
"""

<CustomDropDown>:
    Button:
        text: "Test1"
        size_hint_y: None
        height: 30
        
    Button:
        text: "Test2"
        size_hint_y: None
        height: 30
        
    Button:
        text: "Test3"
        size_hint_y: None
        height: 30
        
    Button:
        text: "Test4"
        size_hint_y: None
        height: 30
        
    Button:
        text: "Test5"
        size_hint_y: None
        height: 30
        
    Button:
        text: "Test6"
        size_hint_y: None
        height: 30

<BoxLayout>:
    orientation: 'horizontal'
    
<Ra>:
    
    cols: 2
    
    BoxLayout:
        
        Label:
            text: "Feedrate: "
            
        TextInput:
            hint_text: "mm/o"
            multiline: False
            write_tab: False
            
    BoxLayout:
        
        Label:
            text:
            

                

"""
)


class Ra(GridLayout):
    
    def custom_callback1(self):
        print('Hello World!')
        
    pass