from kivy.lang import Builder
from kivy.properties import StringProperty, NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput

from Moduler.customwidgets import MyLabel
from Moduler import spiral
from Moduler import ra
from Moduler import datasaving
from Moduler import materialremoval

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
                    TextInput:
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
                    TextInput:
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
                    TextInput:
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
                    TextInput:
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
        
        datasaving.FileHandling().checkfile("Database.xlsx")
        datasaving.CuttingSpeedData("Database.xlsx").filesave(self.txt1.text, self.txt2.text,
                                                              self.txt3.text, self.txt4.text)
            

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
        
    def select(self):
        TextInput().select_all()
        
        