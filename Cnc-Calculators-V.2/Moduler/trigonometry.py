""" This module contains a Trigonometry calculator """

from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty

Builder.load_string(
    """
<Trigonometry>:
    canvas:
        Line:
            points: self.points

    #Button:
    """
)






class Trigonometry(BoxLayout):

    points = ListProperty([(100, 100), (200, 100), (200, 200), (100, 100)])

    pass