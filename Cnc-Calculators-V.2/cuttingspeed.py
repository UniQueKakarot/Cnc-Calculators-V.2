from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout

import MyLabel

Builder.load_string(
"""
    
<BoxLayout>:
    orientation: 'horizontal'

<Label>:
    font_size: 20
    size_hint: 0.5, 1

<TextInput>:
    font_size: 20
    size_hint: 0.5, 1

<CuttingSpeed>:
    orientation: 'vertical'
    
    txt1: cutting
    txt2: mill
    txt3: num_teeth
    txt4: feed_tooth
    grid1: grid1
    box1: box1
    box2: box2
    box3: box3
    box4: box4
    
    TabbedPanel:
        do_default_tab: False
        tab_pos: 'left_top'
        
        TabbedPanelItem:
            text: 'Cutting Data'
            font_size: 15
    
            GridLayout:
                id: grid1
                cols: 1
                padding: 10
                spacing: 5
        
                BoxLayout:
                    id: box1
                    Label:
                        text: 'Cutting Speed:'
                    TextInput:
                        id: cutting
                        multiline: False
                        write_tab: False
                        focus: True
                        text_validate_unfocus: False
                        on_text_validate: root.calc()
        
                BoxLayout:
                    id: box2
                    Label:
                        text: 'Mill Diameter:'
                    TextInput:
                        id: mill
                        multiline: False
                        write_tab: False
                        on_text_validate: root.calc()
        
                BoxLayout:
                    id: box3
                    Label:
                        text: 'Number of Teeth:'
                    TextInput:
                        id: num_teeth
                        multiline: False
                        write_tab: False
                        on_text_validate: root.calc()
        
                BoxLayout:
                    id: box4
                    Label:
                        text: 'Feed per Tooth:'
                    TextInput:
                        id: feed_tooth
                        multiline: False
                        write_tab: False
                        on_text_validate: root.calc()
        
                Button:
                    text: "Calculate!"
                    on_press: root.cuttingspeed.calc()
        
                BoxLayout:
                    Label:
                        text: "Spindle RPM: "
                        font_size: 20
        
                    Label:
                        text: root.res_speed
                        font_size: 20
        
                BoxLayout:
                    MyLabel:
                        text: "Feedrate: "
                        font_size: 20
                        bcolor: [1, 1, 1, 0.2]
        
                    MyLabel:
                        text: root.res_feed
                        font_size: 20
                        bcolor: [1, 1, 1, 0.2]
                        
        TabbedPanelItem:
            text: 'Test'
            font_size: 15
    
"""
)

class CuttingSpeed(BoxLayout):
    
    # Dynamic refrence to the labels that shows the result
    res_speed = StringProperty()
    res_feed = StringProperty()
    
    def __init__(self, **kwargs):
        super(CuttingSpeed, self).__init__(**kwargs)
        
    def calc(self):
        
        """ Main method for the calculations """

        spindel_rpm = self.spindel()
        mill_feed = self.feed(spindel_rpm)

        spindel_rpm = round(spindel_rpm, 0)
        mill_feed = round(mill_feed, 0)

        spindel_rpm = int(spindel_rpm)
        mill_feed = int(mill_feed)

        self.results(spindel_rpm, mill_feed)

    def spindel(self):
        
        """ Method for calculating spindel rpm """
        
        try:
            cs = self.txt1.text
            cs = cs.replace(',', '.')
            cs = float(cs)

            md = self.txt2.text
            md = md.replace(',', '.')
            md = float(md)

            rpm = (cs * 1000) / (3.14 * md)
            
        except ValueError:
            rpm = 0

        return rpm

    def feed(self, spindel_rpm):
        
        """ Method for calculating feedrate """
        
        try:
            nt = self.txt3.text
            nt = nt.replace(',', '.')
            nt = float(nt)

            ft = self.txt4.text
            ft = ft.replace(',', '.')
            ft = float(ft)

            feed_rate = ft * spindel_rpm * nt

        except ValueError:
            feed_rate = 0

        return feed_rate


    def results(self, speed, feed):
        
        """ Method for passing on the results to the gui """

        self.res_speed = str(speed)
        self.res_feed = str(feed)
        
        