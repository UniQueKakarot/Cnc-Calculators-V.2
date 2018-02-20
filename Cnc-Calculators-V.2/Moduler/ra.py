""" This module contains the RA calculator """

from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.properties import StringProperty

from Moduler.customwidgets import MyLabel
from Moduler.customwidgets import MyTextInput
from Moduler.datasaving import SurfaceRaData

Builder.load_string(
    """

<BoxLayout>:
    orientation: 'horizontal'

<MyTextInput>:

<Ra>:

    feed: feed
    nr: nr

    cols: 1
    padding: 10
    spacing: 10

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Feedrate: "

        MyTextInput:
            id: feed
            hint_text: "mm/o"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Nose Radius: "

        MyTextInput:
            id: nr
            hint_text: "mm"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Button:
            text: "Calculate!"
            on_press: root.calc()

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
            text: root.ra
            bcolor: [1, 1, 1, 0.15]

    """
)


class Ra(GridLayout):

    """ Main class for the RA module """

    surface_ra = StringProperty()

    def calc(self):

        """ Calculating RA """

        try:
            feed = self.feed.text
            feed = feed.replace(',', '.')
            feed = float(feed)
        except ValueError:
            pass

        try:
            nose_radius = self.nr.text
            nose_radius = nose_radius.replace(',', '.')
            nose_radius = float(nose_radius)
        except ValueError:
            pass

        try:
            result = ((feed**2) / (nose_radius*24)) * 1000
            result = round(result, 2)
        except(TypeError, ZeroDivisionError):
            result = "Please input values"

        self.surface_ra = str(result)

        SurfaceRaData("Database.xlsx").filesave(self.feed.text,
                                                self.nr.text,
                                                result)
