""" This module hold the material removal calculator"""

from kivy.lang import Builder
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty

from Moduler.customwidgets import MyLabel
from Moduler.customwidgets import MyTextInput
from Moduler.datasaving import MaterialRemovalData

Builder.load_string(
    """
<MaterialRemoval>:
    cols: 1
    padding: 10
    spacing: 7

    # text input id's
    ap: ap
    ae: ae
    feed: feed

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Depth of cut: "

        MyTextInput:
            id: ap
            hint_text: "ap"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Width of cut: "

        MyTextInput:
            id: ae
            hint_text: "ae"
            multiline: False
            write_tab: False
            on_text_validate: root.calc()

    BoxLayout:
        size_hint_y: None
        height: "40dp"
        Label:
            text: "Feedrate: "

        MyTextInput:
            id: feed
            hint_text: "mm/m"
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
            text: "Material Removal Rate:"
            font_size: 20
            bcolor: [1, 1, 1, 0.15]

        MyLabel:
            text: root.res_mrr
            font_size: 20
            bcolor: [1, 1, 1, 0.15]


    """
)


class MaterialRemoval(GridLayout):

    """ Main class for the MRR module """

    res_mrr = StringProperty()

    def calc(self):

        """ Entry method for the calculations """

        result = self.mrrcalc()
        self.results(result)

        MaterialRemovalData("Database.xlsx").filesave(self.ap.text,
                                                      self.ae.text,
                                                      self.feed.text,
                                                      result)

    def mrrcalc(self):

        """ Getting the values and doing the calculation """

        try:
            cut_depth = self.ap.text
            cut_depth = cut_depth.replace(',', '.')
            cut_depth = float(cut_depth)
        except ValueError:
            pass

        try:
            cut_width = self.ae.text
            cut_width = cut_width.replace(',', '.')
            cut_width = float(cut_width)
        except ValueError:
            pass

        try:
            feed = self.feed.text
            feed = feed.replace(',', '.')
            feed = float(feed)
        except ValueError:
            pass

        # doing the calculation
        try:
            mrr = (cut_depth * cut_width * feed) / 1000
        except (ValueError, TypeError):
            mrr = "Please input values"

        return mrr

    def results(self, result):

        """ Updating the UI label with the result """

        result = str(result)
        result = (result + ' cm³/min')

        self.res_mrr = str(result)
