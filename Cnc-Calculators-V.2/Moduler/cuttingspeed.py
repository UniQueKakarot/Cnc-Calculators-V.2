""" This module hold the Cutting Data calculator and also works as the root
    widget for all the other modules in this software  """

from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

from Moduler.customwidgets import MyLabel
from Moduler.customwidgets import MyTextInput
from Moduler.datasaving import CuttingSpeedData
from Moduler import spiral
from Moduler import ra
from Moduler import materialremoval

# this modules kvlang definition
Builder.load_string(
    """
<BoxLayout>:
    orientation: 'horizontal'

<Label>:
    font_size: 20

<TextInput>:
    font_size: 20

<CuttingSpeed>:
    orientation: 'vertical'

    txt1: cutting
    txt2: mill
    txt3: num_teeth
    txt4: feed_tooth
    grid1: grid1

    TabbedPanel:
        do_default_tab: False
        tab_pos: 'top_left'
        tab_height: 25
        tab_width: 125

        TabbedPanelItem:
            text: 'Cutting Data'
            font_size: 15

            GridLayout:
                id: grid1
                cols: 1
                padding: 10
                spacing: 7

                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: 'Cutting Speed:'
                    MyTextInput:
                        id: cutting
                        hint_text: "m/min"
                        multiline: False
                        write_tab: False
                        focus: True
                        on_text_validate: root.calc()

                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: 'Mill Diameter:'
                    MyTextInput:
                        id: mill
                        hint_text: "ø"
                        multiline: False
                        write_tab: False
                        on_text_validate: root.calc()

                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: 'Number of Teeth:'
                    MyTextInput:
                        id: num_teeth
                        hint_text: "z"
                        multiline: False
                        write_tab: False
                        on_text_validate: root.calc()

                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: 'Feed per Tooth:'
                    MyTextInput:
                        id: feed_tooth
                        hint_text: "mm/o"
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
                    Label:
                    #Image:
                        #source: "D:\Iver\Bilder\Kivy\Cnc-CalcV2\Test.png"

                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    Label:
                        text: "Spindle RPM: "
                        font_size: 20

                    Label:
                        text: root.res_speed
                        font_size: 30

                BoxLayout:
                    size_hint_y: None
                    height: "40dp"
                    MyLabel:
                        text: "Feedrate: "
                        font_size: 20
                        bcolor: [1, 1, 1, 0.2]

                    MyLabel:
                        text: root.res_feed
                        font_size: 30
                        bcolor: [1, 1, 1, 0.2]

        TabbedPanelItem:
            text: 'MRR'
            font_size: 15
            MaterialRemoval:

        TabbedPanelItem:
            text: 'Toolpath Angle'
            font_size: 15
            Spiral:

        TabbedPanelItem:
            text: 'Ra'
            font_size: 15
            Ra:


    """
)


class CuttingSpeed(BoxLayout):

    """ Main class for the Cutting Data calculator """

    # Dynamic refrence to the labels that shows the result
    res_speed = StringProperty()
    res_feed = StringProperty()

    def calc(self):

        """ Main method for the calculations """

        spindel_rpm = self.spindel()
        mill_feed = self.feed(spindel_rpm)

        spindel_rpm = round(spindel_rpm, 0)
        mill_feed = round(mill_feed, 0)

        spindel_rpm = int(spindel_rpm)
        mill_feed = int(mill_feed)

        self.results(spindel_rpm, mill_feed)

        CuttingSpeedData("Database.xlsx").filesave(self.txt1.text,
                                                   self.txt2.text,
                                                   self.txt3.text,
                                                   self.txt4.text)

    def spindel(self):

        """ Method for calculating spindel rpm """

        try:
            cutting_speed = float(self.txt1.text.replace(',', '.'))

            mill_dia = float(self.txt2.text.replace(',', '.'))

            rpm = (cutting_speed * 1000) / (3.14 * mill_dia)

        except ValueError:
            rpm = 0

        return rpm

    def feed(self, spindel_rpm):

        """ Method for calculating feedrate """

        try:
            num_of_teeth = float(self.txt3.text.replace(',', '.'))

            feed_pr_tooth = float(self.txt4.text.replace(',', '.'))

            feed_rate = feed_pr_tooth * spindel_rpm * num_of_teeth

        except ValueError:
            feed_rate = 0

        return feed_rate

    def results(self, speed, feed):

        """ Method for passing on the results to the gui """

        self.res_speed = str(speed)
        self.res_feed = str(feed)
