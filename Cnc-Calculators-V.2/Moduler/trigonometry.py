""" This module contains a Trigonometry calculator """

from math import sin, degrees, radians

from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ListProperty
from kivy.uix.checkbox import CheckBox

from Moduler.customwidgets import MyLabel
from Moduler.customwidgets import MyTextInput

Builder.load_string(
    """
<Trigonometry>:

    aa: aa
    ac: ac
    sa: sa

    canvas:
        Line:
            points: self.points

    BoxLayout:
        orientation: "vertical"
        size_hint_y: None
        height: "150dp"
        padding: 10
        spacing: 7
        #size_hint_x: 0.3
        #pos: 0, 460
        BoxLayout:
            size_hint_y: None
            height: "40dp"
            Label:
                text: "Angle A"

            MyTextInput:
                id: aa
                hint_text:
                multiline: False
                write_tab: False
                on_text_validate:

        BoxLayout:
            size_hint_y: None
            height: "40dp"
            Label:
                text: "Angle C"

            MyTextInput:
                id: ac
                hint_text:
                multiline: False
                write_tab: False
                on_text_validate:        

        BoxLayout:
            size_hint_y: None
            height: "40dp"
            #size_hint_x: 0.3
            #pos: 0, 360
            Label:
                text: "Side b"

            MyTextInput:
                id: sa
                hint_text:
                multiline: False
                write_tab: False
                on_text_validate:

    BoxLayout:
        size_hint_y: None
        height: "187"
        size_hint_x: None
        width: "220"
        pos: 450, 330
        Image:
            source: "triangle.png"

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        size_hint_x: None
        width: "100dp"
        pos: 0, 200
        Label:
            text: "Test 1"
        CheckBox:


    BoxLayout:
        size_hint_y: None
        height: "40dp"
        size_hint_x: 0.3
        pos: 450, 200
        Button:
            text: "Run"
            on_press: root.test()

    """
)

class MyCheckBox(CheckBox):
    pass

class Trigonometry(GridLayout):

    cols = 2

    points = ListProperty()

    def test(self):

        # converting angle a from text to int
        angle_a = self.aa.text
        angle_a = int(angle_a)

        # converting angle c from text to int
        angle_c = self.ac.text
        angle_c = int(angle_c)

        # converting the length of side a from text to int
        side_a = self.sa.text
        side_a = int(side_a)

        # calculating angle b from whats left
        angle_b = 180 - angle_a - angle_c

        # python sure loves it radians
        angle_a = radians(angle_a)
        angle_c = radians(angle_c)
        angle_b = radians(angle_b)

        # doing the math for the opposite
        opposite = (sin(angle_a) * side_a) / sin(angle_b)

        # doing the math for the hypotenuse
        hypotenuse = (sin(angle_c) * side_a) / sin(angle_b)

        print(angle_b, '\n')
        print(opposite, '\n')
        print(hypotenuse)

        test = 250 + opposite

        # assigning my listproperty some values to draw a triangle
        self.points = [(100, 250), (300, 250), (300, test), (100, 250)]

        #TODO
        # made some headway on drawing the triangle after the calculations
        # so now i have to decide if i want the length of the triangle
        # to represent the drawn triangle, which might be a cool thing to do
        # position needs more consideration and how do we present the results?
