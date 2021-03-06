""" This module hold the Helix angle calculator """

from math import sin, degrees
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty
from kivy.lang import Builder

from Moduler.customwidgets import MyLabel
from Moduler.customwidgets import MyTextInput
from Moduler import straight
from Moduler.datasaving import HelixData

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
            text: 'Helix Angle'
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
                        text: root.res_angle
                        font_size: 20
                        bcolor: [1, 1, 1, 0.15]

        TabbedPanelItem:
            text: 'Ramp Angle'
            font_size: 15
            Straight:

    """
)

class Spiral(FloatLayout):

    """ Main class for the Helix angle module """

    res_angle = StringProperty()

    def calc(self):

        """ Entry method for the calculations """

        circumference = self.circumference()
        angle = self.angle(circumference)

        self.results(angle)

        HelixData("Database.xlsx").filesave(self.milldia.text,
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

            circumference = (holedia - milldia) * 3.14
        except ValueError:
            circumference = 0

        return circumference

    def angle(self, circumference):

        """ Calculating the angle of the toolpath """

        try:
            zstep = self.zstep.text
            zstep = zstep.replace(',', '.')
            zstep = float(zstep)

            angle = (sin(1.57079633) * zstep) / circumference
            angle = degrees(angle)
        except(ValueError, ZeroDivisionError):
            angle = "Please input values"

        try:
            return round(angle, 2)
        except TypeError:
            angle = "Please input values"
            return angle

    def results(self, angle):

        """ Updating the UI label with the results """

        self.res_angle = str(angle)
