""" This module contains the Ramp angle calculator """

from math import sin, degrees
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

from Moduler.customwidgets import MyLabel
from Moduler.customwidgets import MyTextInput
from Moduler.datasaving import RampData

Builder.load_string(
    """

<BoxLayout>:
    orientation: 'horizontal'

<Label>:
    font_size: 20

<TextInput>:
    font_size: 20

<Straight>:

    tpl: tpl
    zstep: zstep

    cols: 1
    padding: 10
    spacing: 10

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Toolpath Lenght: "
        MyTextInput:
            id: tpl
            hint_text: "mm"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Step/Pitch: "
        MyTextInput:
            id: zstep
            hint_text: "Z Step"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Button:
            text: "Calculate!"
            on_press: root.calc()

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

    """ Main class for the Ramp Angle module """

    angle = StringProperty()

    def calc(self):

        """ Doing the mathy thingy """

        try:
            tpl = self.tpl.text
            tpl = tpl.replace(',', '.')
            tpl = float(tpl)
        except ValueError:
            pass

        try:
            zstep = self.zstep.text
            zstep = zstep.replace(',', '.')
            zstep = float(zstep)
        except ValueError:
            pass

        try:
            result = (sin(1.570796) * zstep) / tpl
            result = degrees(result)
            result = round(result, 2)
        except (ZeroDivisionError, TypeError):
            result = "Please input values"

        self.angle = str(result)

        RampData("Database.xlsx").filesave(self.tpl.text,
                                           self.zstep.text,
                                           result)
