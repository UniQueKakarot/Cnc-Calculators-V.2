""" This module contains a Trigonometry calculator """

from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ListProperty

from Moduler.customwidgets import MyLabel
from Moduler.customwidgets import MyTextInput

Builder.load_string(
    """
<Trigonometry>:
    canvas:
        Line:
            points: self.points

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        size_hint_x: 0.3
        pos: 0, 480
        Label:
            text: "Angle A"

        MyTextInput:
            hint_text:
            multiline: False
            write_tab: False
            on_text_validate:

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        size_hint_x: 0.3
        pos: 0, 430
        Label:
            text: "Angle B"

        MyTextInput:
            hint_text:
            multiline: False
            write_tab: False
            on_text_validate:

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        size_hint_x: 0.3
        pos: 0, 380
        Label:
            text: "Side A"

        MyTextInput:
            hint_text:
            multiline: False
            write_tab: False
            on_text_validate:


    #Button:
    """
)


class Trigonometry(FloatLayout):

    points = ListProperty([(100, 100), (200, 100), (200, 200), (100, 100)])

    pass