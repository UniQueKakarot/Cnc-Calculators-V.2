from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.lang import Builder
from math import sin, degrees

from Moduler.customwidgets import MyLabel
from Moduler.customwidgets import MyTextInput
from Moduler import straight
from Moduler import datasaving

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
    milldia: milldia
    holedia: holedia
    zstep: zstep

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

                    MyTextInput:
                        id: milldia
                        focus: True
                        hint_text: "ø"
                        on_text_validate: root.calc()

                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: "Hole Diameter:"

                    MyTextInput:
                        id: holedia
                        hint_text: "ø"
                        on_text_validate: root.calc()

                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: "Step/Pitch:"

                    MyTextInput:
                        id: zstep
                        hint_text: "Z step"
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
                        text: root.res_angle
                        font_size: 20
                        bcolor: [1, 1, 1, 0.15]

        TabbedPanelItem:
            text: 'Straigth'
            font_size: 15
            Straight:

    """
)

class Spiral(FloatLayout):

    res_angle = StringProperty()

    def __init__(self, **kwargs):
        super(Spiral, self).__init__(**kwargs)

    def calc(self):

        circumference = self.circumference()
        angle = self.angle(circumference)

        self.results(angle)

        datasaving.SpiralData("Database.xlsx").filesave(self.milldia.text,
                                                        self.holedia.text,
                                                        self.zstep.text,
                                                        angle)

    def circumference(self):

        """ Calculating the circumference of the path the mill will be taking """

        try:
            milldia = self.milldia.text
            milldia = milldia.replace(',', '.')
            milldia = float(milldia)

            holedia = self.holedia.text
            holedia = holedia.replace(',', '.')
            holedia = float(holedia)

            cf = (holedia - milldia) * 3.14
        except ValueError:
            cf = 0

        return cf

    def angle(self, circumference):

        """ Calculating the angle of the toolpath """

        cf = circumference

        try:
            zstep = self.zstep.text
            zstep = zstep.replace(',', '.')
            zstep = float(zstep)

            angle = (sin(1.57079633) * zstep) / cf
            angle = degrees(angle)
        except(ValueError, ZeroDivisionError):
            angle = "Please input values"

        return round(angle, 2)

    def results(self, angle):

        """ Updating the UI label with the results """

        self.res_angle = str(angle)
