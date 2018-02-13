from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from math import sin, degrees

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
        TextInput:
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
        TextInput:
            id: zstep
            hint_text: "Z Step"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Button:
            text: "Calculate"
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
            pass




        self.angle = str(result)
