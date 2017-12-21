from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_string(
"""

<Ra>:
    
    cols: 2
    
    BoxLayout:
        orientation: 'vertical'
        
        Button:
            text: "Page 1"
            on_press: root.custom_callback1()  
        Button:
            text: "Page 2"
            on_press:
        Button:
            text: "Page 3"

"""
)


class Ra(GridLayout):
    
    def custom_callback1(self):
        print('Hello World!')
        
    pass