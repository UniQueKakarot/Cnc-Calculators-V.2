from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.textinput import TextInput

from Moduler.customwidgets import MyLabel

Builder.load_string(
"""

<BoxLayout>:
    orientation: 'horizontal'

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

        TextInput:
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

class MyTextInput(TextInput):

    def on_focus(self, instance, value):
        if value:
            print('User focused', instance)
        else:
            print('User defocused', instance)


class Ra(GridLayout):
    ra = StringProperty()

    def calc(self):

        try:
            feed = self.feed.text
            feed = feed.replace(',', '.')
            feed = float(feed)
        except ValueError:
            pass

        try:
            nr = self.nr.text
            nr = nr.replace(',', '.')
            nr = float(nr)
        except ValueError:
            pass

        try:
            result = ((feed**2) / (nr*24)) * 1000
            result = round(result, 2)
        except(TypeError, ZeroDivisionError):
            result = "Please input valid values"

        self.ra = str(result)